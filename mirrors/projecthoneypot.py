#!/usr/bin/env python3
import requests
import re

def download_file(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0'  # Avoid download block  
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses  
        return response.text  
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file from {url}. Error: {e}")
        return None

def extract_ips(text):
    ip_pattern = r'(?:(?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?'
    return re.findall(ip_pattern, text)

def read_existing_ips(filename):
    try:
        with open(filename, 'r') as file:
            return set(file.read().splitlines())  # Return a set of unique IPs from the existing file  
    except FileNotFoundError:
        print(f"{filename} not found. Assuming it has 0 IPs.")
        return set()  # Return an empty set if the file does not exist
    
def save_ips(urls, filename):
    unique_ips = set()  # Initialize a set to store unique IPs (on every run)
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
   'https://www.projecthoneypot.org/list_of_ips.php?t=h&rss=1',  # Replace with your URLs
   'https://www.projecthoneypot.org/list_of_ips.php?t=s&rss=1',
   'https://www.projecthoneypot.org/list_of_ips.php?t=w&rss=1',
   'https://www.projecthoneypot.org/list_of_ips.php?t=p&rss=1',
   'https://www.projecthoneypot.org/list_of_ips.php?t=d&rss=1',
   'https://www.projecthoneypot.org/list_of_ips.php?t=r&rss=1',
   'https://www.projecthoneypot.org/list_of_ips.php?t=se&rss=1',
   'http://www.projecthoneypot.org/list_of_ips.php?uag=115772&rss=1'
]

save_ips(urls, 'projecthoneypot.txt')
