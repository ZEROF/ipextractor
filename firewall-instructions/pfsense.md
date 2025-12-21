
![pfsense logo](images/pfsense_logo.png)

## PfSense Instructions

On the project page https://ipex.root.rodeo, we can find the raw link for file *ipexdbl.txt* which contains Ipex DBL IP's.

Next, go to the Firewall Aliases in PfSense, and add a new one :

![pfsense alias settings](images/pfsense_alias_1.png)

In the next step we give name to alias, short description and very important we chose the type: URL Table. And we add URL with IPEX DBL ip's.

![pfsense alias settings](images/pfsense_alias_2.png)

Save this configuration and move to the next step. Setting firewall rule.

Configure the rule with the following settings:

Action: Block
Protocol: IPv4
Source: “Single host or alias” and enter the name of the alias created in the previous step (IPEXDBL)
Destination: any​

![pfsense firewall settings](images/pfsense_firewall_rule.png)

This rule must be on the top of your rules. And we checked "Log" option to be able to see blocked IP's in the firewall logs.

![pfsense firewall settings](images/pfsense_firewall_rule_order.png)

By default, pfSense updates URL rules every 24 hours, while IPEX DBL updates every 4 hours. To align schedules, install the pfSense "Cron" package and make the following small modification in the cron settings:

![pfsense cron settings](images/pfsense_cron.png)

Edit cron job to fit settings:

![pfsense cron settings](images/pfsense_cron_1.png)
![pfsense cron settings](images/pfsense_cron_2.png)

Save settings and you are ready to watch blocked traffic in PfSense logs:

![pfsense ipx dbl in action](images/pfsense_ipex_dbl_in_action.png)