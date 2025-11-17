
# IPEx DBL
<p style="margin-left: auto;margin-right: auto;">
<b> IP Extractor for IPEX Dynamic Block List (s) </b>
</p>
<div style="margin-left: auto;
            margin-right: auto;
            width: 40%">
<img src="website/images/ipextractor.png"  alt="Pixabay free firewall image" width="220" height="180">
</div>

The number of IP block lists available for use with firewalls is huge, including among others, Spamhaus, Crowdsec, BinaryDefence BlocklistDE and DShield. This project aims to consolidate the most effective block lists. The PoC for this project was a six-month journey of exploration and I don't have feeling that it's done.

Using a block list in conjunction with firewalls is a critical strategy for enhancing network security and effectively combating malicious actors. A block list, also known as a blacklist, is a list of IP addresses, domains, or URLs that are known to be associated with malicious activity. By implementing a block list, organizations can proactively prevent access to harmful content and reduce the risk of cyber threats.

##### Why opt for IPEX DBL list rather than other available choices:

1. Our PoC demostrated that list with 15000 entries sometimes get reduced to only 7000. This means that these lists duplicate one another or utilize identical data sources. 
2. You can quickly set your firewall aliases and related policies without the usual plugin hassle.
3. The lists are updated every 4 hours if there is fresh information available from the source. This ensures that IPEX dynamic list receive the most current and relevant data.
4. This is an open source project, and the list is maintained clean, without any additional inputs (publicity) that could create problems for some firewalls.
5. IPEX manage own honeypots, we call them IPEX Hunters. We learn from working on them and we take time to assure flowless integration.

#### Supported firewalls

Instructions for [PfSense](https://www.provya.com/blog/pfsense-opnsense-blocking-bad-risky-ip-addresses/)

Instruction for [Opensense](https://github.com/ZEROF/ipextractor/blob/main/firewall-instructions/opensense.md)

Instruction for [Fortigate](https://github.com/ZEROF/ipextractor/blob/main/firewall-instructions/fortigate.md)

Instruction for [OpenWRT](https://github.com/ZEROF/ipextractor/blob/main/firewall-instructions/openwrt.md)

`` Use 'RAW' URL (ipexdbl.txt) from this repository for seamless integration with your firewall. ``

#### ipexdbl.txt extracted from :

1. IPEX Hunters
2. BinaryDefense
3. DShield
4. Crowdsec
5. Bruteforce
6. Talos
7. BlocklistDE
8. ProjectHoneypot
9. Spamhaus
10. Threatfox

#### ipexdbl_simple.txt extracted from:
1. Spamhaus

#### TO DO LIST
- [x] Host full HPP mirror
- [x] Add ipexhunters.txt (integrate IPEX project honeypots list.)
- [x] Add projecthoneypot.org RSS feed (beta)
- [x] Instuction for firewalls (listed above), if someone have instructions for other firewalls, please open issue
- [x] Better README
- [x] Add CrowdSec private mirror
- [x] Add Talos block list
- [x] Host block list(s) mirror(s): only to show working solution for some sources.
- [x] Create web home for this repository (ipex.something.x) (not hosted yet, simple html finished)
- [x] GitHub Actions: block run if errors are detected
- [x] Merge updated list(s) after running GitHub Actions
- [x] Python: don't stop updating list(s) if source is sending error 400
- [ ] IPEX is inbound traffic dynamic block list, but outbound DBL can exist as well (PoC and more information are needed)
- [x] Integration of IPEX Hunters honeypots (for now only endlessh backend used)
- [ ] Integrate web honeypotting to IPEX Hunters 
- [x] Add local version for Fortigate settings

### Support our project

- VPS and SERVER donations are accepted (we will hunt bad actors for you)

Project supported by:

https://glesys.com

 <img width="300" alt="Lockup Black" src="https://github.com/user-attachments/assets/80c895e1-7a7e-4f7d-8618-50e585d440f3" />

https://www.neocloud.rs

![image](https://github.com/user-attachments/assets/3248351d-76b2-4075-b1c9-9171b8a10951)

### Repo layout
```
ipextractor
├── LICENSE
├── README.md
├── firewall-instructions
│   ├── fortigate.md
│   ├── images
│   │   ├── opensense_alias_1.png
│   │   ├── opensense_alias_2.png
│   │   ├── opensense_alias_3.png
│   │   ├── opensense_floating_block_rule.png
│   │   ├── opensense_floating_rule.png
│   │   ├── opensense_label_logview.png
│   │   ├── opensense_logo.png
│   │   ├── opensense_packets_tag.png
│   │   ├── openwrt_banip_1.png
│   │   ├── openwrt_banip_2.png
│   │   └── openwrt_logo.png
│   ├── opensense.md
│   └── openwrt.md
├── ipexdbl.py
├── ipexdbl.txt
├── ipexdbl_simple.py
├── ipexdbl_simple.txt
├── mirrors
│   └── projecthoneypot.py
└── website
    ├── CHANGELOG.md
    ├── README-Docker.md
    ├── docker-compose.yml
    ├── images
    │   └── ipextractor.png
    └── index.html
```
