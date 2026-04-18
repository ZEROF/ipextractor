#!/usr/bin/env python3
"""
Download IP block-lists from several public sources, de-duplicate them,
and drop any single address that is already covered by a /24 that is
present in the same list.
"""

import requests
import re


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def download_file(url: str) -> str | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "X-Custom-Header": "Let me in",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.RequestException as exc:
        print(f"Failed to download {url}  –  {exc}")
        return None


def extract_ips(text: str) -> list[str]:
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}(?:/24)?\b"
    potential = re.findall(ip_pattern, text)
    valid = []

    for raw in potential:
        base, _, suffix = raw.partition("/")
        octets = base.split(".")
        if len(octets) != 4:
            continue
        try:
            octets_int = [int(o) for o in octets]
        except ValueError:
            continue
        if not all(0 <= x <= 255 for x in octets_int):
            continue

        if suffix == "24":  # always keep /24
            valid.append(raw)
        else:  # drop x.y.0 or x.y.0.0
            if not (base.endswith(".0") or base.endswith(".0.0")):
                valid.append(base)  # store without /24
    return valid


def _remove_covered_by_cidr(ip_set: set[str]) -> set[str]:
    """
    Remove single IPs that fall inside a /24 already present in the set.
    """
    cidrs = {ip for ip in ip_set if "/" in ip}
    singles = {ip for ip in ip_set if "/" not in ip}

    # 3-octet prefixes for which we have a /24
    covered_24 = {ip.split("/")[0].rsplit(".", 1)[0] for ip in cidrs}

    # keep singles whose 3-octet prefix is NOT covered
    filtered = {ip for ip in singles if ip.rsplit(".", 1)[0] not in covered_24}

    return cidrs | filtered


def read_existing_ips(filename: str) -> set[str]:
    try:
        with open(filename) as fh:
            return set(fh.read().splitlines())
    except FileNotFoundError:
        return set()


# ------------------------------------------------------------------
# Main workflow
# ------------------------------------------------------------------
def save_ips(urls: list[str], filename: str) -> None:
    unique_ips = set()
    for url in urls:
        content = download_file(url)
        if content:
            ips = extract_ips(content)
            unique_ips.update(ips)
            print(f"Fetched {len(ips):5} IPs  –  {url}")

    existing = read_existing_ips(filename)
    print(f"Old file contained {len(existing)} unique IPs")

    # *** NEW: drop singles covered by a /24 ***
    unique_ips = _remove_covered_by_cidr(unique_ips)

    with open(filename, "w") as fh:
        for ip in sorted(unique_ips):
            fh.write(ip + "\n")

    new_count, old_count = len(unique_ips), len(existing)
    print(f"Saved {new_count} unique IPs to {filename}")
    print(f"Difference: {new_count - old_count:+d}  (new {new_count}, old {old_count})")


# ------------------------------------------------------------------
# Run
# ------------------------------------------------------------------
if __name__ == "__main__":
    URLS = [
        "https://www.spamhaus.org/drop/drop.txt",
        "https://www.binarydefense.com/banlist.txt",
        "https://raw.githubusercontent.com/UoFruitE/ProcessedLists/main/processed_dshield.txt",
        "https://lists.blocklist.de/lists/all.txt",
        "https://crowdsec.root.rodeo/security/blocklist",
        "https://ipex.root.rodeo/talos.txt",
        "https://opendbl.net/lists/bruteforce.list",
        "https://ipex.root.rodeo/projecthoneypot.txt",
        "https://ipex.root.rodeo/ipexhunters.txt",
        "https://ipex.root.rodeo/fortigatehoneypot.txt",
    ]
    save_ips(URLS, "ipexdbl.txt")
