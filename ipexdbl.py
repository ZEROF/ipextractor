#!/usr/bin/env python3
import requests
import re

def download_file(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',  # Avoid download block new version
        'X-Custom-Header': 'Let me in' # Add custom headet to bypass binarydefense 
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses  
        return response.text  
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file from {url}. Error: {e}")
        return None

def extract_ips(text):
    # Step 1: Extract all potential IPs (with optional /24)
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}(?:\/24)?\b'
    potential_ips = re.findall(ip_pattern, text)
    
    valid_ips = []
    for ip in potential_ips:
        # Separate base IP and suffix
        parts = ip.split('/')
        base_ip = parts[0]
        suffix = parts[1] if len(parts) > 1 else None
        
        # Validate octets
        octets = base_ip.split('.')
        if len(octets) != 4:
            continue
            
        try:
            octets_int = [int(octet) for octet in octets]
        except ValueError:
            continue
            
        if not all(0 <= x <= 255 for x in octets_int):
            continue
            
        # Step 2: Apply filtering rules
        if suffix == '24':
            # Always keep /24 addresses
            valid_ips.append(ip)
        else:
            # For non-/24 addresses, remove if ends with .0 or .0.0
            if not (base_ip.endswith('.0') or base_ip.endswith('.0.0')):
                valid_ips.append(ip)
                
    return valid_ips

def read_existing_ips(filename):
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())  # Return a set of unique IPs from the existing file  
    except FileNotFoundError:
        print(f"{filename} not found. Assuming it has 0 IPs.")
        return set()  # Return an empty set if the file does not exist
    
def save_ips(urls, filename):
    unique_ips = set()  # Initialize a set to store unique IPs
    for url in urls:
        file_content = download_file(url)
        if file_content:
            ip_addresses = extract_ips(file_content)
            unique_ips.update(ip_addresses)  # Add new IPs to the set
            print(f"Found {len(ip_addresses)} IPs from {url}") # Print the count of IPs for each URL
 
    existing_ips = read_existing_ips(filename)  # Read IPs from old file  
    print(f"Old file has {len(existing_ips)} unique IPs.")
 
    with open(filename, 'w') as file:
        for ip in sorted(unique_ips):  # Sort IPs for better readability
            file.write(ip + '\n')
    print(f"Saved {len(unique_ips)} unique IP addresses to {filename}")
  
    # Calculate and display the difference in IP counts  
    new_count = len(unique_ips)
    old_count = len(existing_ips)
    difference = new_count - old_count  
    print(f"Difference in number of IPs: {difference} (New: {new_count}, Old: {old_count})")

# Example usage
urls = [
    'https://www.spamhaus.org/drop/drop.txt',  # Replace with your URLs
    'https://www.binarydefense.com/banlist.txt',
    'https://raw.githubusercontent.com/UoFruitE/ProcessedLists/main/processed_dshield.txt',
    'https://lists.blocklist.de/lists/all.txt',
    'https://crowdsec.root.rodeo/security/blocklist',
    'https://ipex.root.rodeo/talos.txt',
    'https://opendbl.net/lists/bruteforce.list',
    'https://ipex.root.rodeo/projecthoneypot.txt',
    'https://ipex.root.rodeo/ipexhunters.txt',
    'https://threatfox.abuse.ch/export/json/recent'
]

save_ips(urls, 'ipexdbl.txt')
