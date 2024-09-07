# ipextractor #
### Extract IP addresses from text files using python and create firewall IP block list

The number of IP block lists available for use with firewalls is huge, including among others, options like Spamhaus, Crowdsec, BinaryDefence BlocklistDE and DShield. This project aims to consolidate the most effective block lists. The PoC for this project was a six-month journey of exploration and I don't have feeling that it's done.


Using a block list in conjunction with firewalls is a critical strategy for enhancing network security and effectively combating malicious actors. A block list, also known as a blacklist, is a list of IP addresses, domains, or URLs that are known to be associated with malicious activity. By implementing a block list, organizations can proactively prevent access to harmful content and reduce the risk of cyber threats.

#### Supported firewalls

Instructions for [PfSense](https://www.provya.com/blog/pfsense-opnsense-blocking-bad-risky-ip-addresses/)

Instruction for [Opensense](https://docs.opnsense.org/manual/how-tos/edrop.html)

Instruction for [Fortigate](https://docs.fortinet.com/document/fortigate/7.2.4/administration-guide/891236/ip-address-threat-feed)

`` Use 'RAW' URL (extracted_multi_ips.txt) from this repository for seamless integration with your firewall. ``

#### Included lists in extracted_multi_ips.txt:

1. Spamhaus
2. BinaryDefense
3. DShield
4. Crowdsec
5. Bruteforce
6. Talos
7. BlocklistDE

#### Included list in "extracted_simple_ips.txt
1. Spamhaus

#### TO DO LIST

- [x] Instuction for firewalls (listed above), if someone have instructions for other firewalls, please open case
- [x] Better README
- [x] Add CrowdSec private mirror
  [x] Add Talos block list
- [ ] Host block list(s) mirror(s) (selfhosted on the secondary domain)
- [ ] Create web home for this repository (ipexblock.something.x)
- [x] GitHub Actions: block run if errors are detected
- [x] Merge updated list(s) after running GitHub Actions
- [x] Python: don't stop updating list(s) if source is sending error 400

