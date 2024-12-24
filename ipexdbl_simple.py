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
    

def save_ips(ips, filename):
    unique_ips = set(ips)  # Remove duplicates
    with open(filename, 'w') as file:
        for ip in sorted(unique_ips):  # Sort IPs for better readability
            file.write(ip + '\n')
    print(f"Saved {len(unique_ips)} unique IP addresses to {filename}")

# Example usage
url = 'https://www.spamhaus.org/drop/drop.txt'  # Replace with your URL
file_content = download_file(url)

if file_content:
    ip_addresses = extract_ips(file_content)
    save_ips(ip_addresses, 'ipexdbl_simple.txt')
