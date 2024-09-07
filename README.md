# ipextractor #
### Extract IP addresses from text files using python and create firewall IP block list

The number of IP block lists available for use with firewalls is huge, including among others, options like Spamhaus, Crowdsec, BinaryDefence BlocklistDE and DShield. This project aims to consolidate the most effective block lists. The PoC for this project was a six-month journey of exploration and I don't have feeling that it's done.


Using a block list in conjunction with firewalls is a critical strategy for enhancing network security and effectively combating malicious actors. A block list, also known as a blacklist, is a list of IP addresses, domains, or URLs that are known to be associated with malicious activity. By implementing a block list, organizations can proactively prevent access to harmful content and reduce the risk of cyber threats.

#### Supported firewalls

How to use with PfSense: "For now everyone can send url proposal"

How to use with OpenSense: "For now everyone can send url proposal"

How to use with FortiGate: "For now everyone can send url proposal"

`` You can already utilize the 'RAW' URL's from this repository for seamless integration with your firewall. ``

#### Included lists in extracted_multi_ips.txt:

1. Spamhaus
2. BinaryDefense
3. DShield
4. Crowdsec
5. Bruteforce
6. Talos

#### Included list in "extracted_simple_ips.txt
1. Spamhaus

#### TO DO LIST

- [ ] Instuction for firewalls (listed above), if someone have instructions about other firewalls, please contact me (ticket)
- [ ] Better README
- [x] Add CrowdSec private mirror
  [x] Add Talos block list
- [ ] Host block list(s) mirror(s) (selfhosted on the secondary domain)
- [ ] Create web home for this repository (ipexblock.something.x)
- [x] GitHub Actions: block run if errors are detected
- [x] Merge updated list(s) after running GitHub Actions
- [x] Python: don't stop updating list(s) if source is sending error 400

