#!/usr/bin/env python3
import requests
import re

def download_file(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to download file.")
        return None

def extract_ips(text):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
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
    save_ips(ip_addresses, 'extracted_simple_ips.txt')
