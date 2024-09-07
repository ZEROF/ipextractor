#!/usr/bin/env python3
import requests
import re

def download_file(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0' # Avoid download block
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download file from {url}.")
        return None

def extract_ips(text):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ip_pattern, text)

def save_ips(urls, filename):
    unique_ips = set()  # Initialize a set to store unique IPs
    for url in urls:
        file_content = download_file(url)
        if file_content:
            ip_addresses = extract_ips(file_content)
            unique_ips.update(ip_addresses)  # Add new IPs to the set

    with open(filename, 'w') as file:
        for ip in sorted(unique_ips):  # Sort IPs for better readability
            file.write(ip + '\n')
    print(f"Saved {len(unique_ips)} unique IP addresses to {filename}")

# Example usage
urls = [
    'https://www.spamhaus.org/drop/drop.txt',  # Replace with your URLs
    'https://www.binarydefense.com/banlist.txt',
    'https://raw.githubusercontent.com/UoFruitE/ProcessedLists/main/processed_dshield.txt',
    'https://opendbl.net/lists/blocklistde-all.list',
    'https://opendbl.root.rodeo/security/blocklist',
    'https://opendbl.net/lists/talos.list',
    'https://opendbl.net/lists/bruteforce.list'
]

save_ips(urls, 'extracted_multi_ips.txt')
