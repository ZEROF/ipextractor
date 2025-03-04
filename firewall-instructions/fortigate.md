# IP address threat feed | FortiGate / FortiOS 7.x
IP address threat feed
----------------------

An IP address threat feed is a dynamic list that contains IPv4 and IPv6 addresses, address ranges, and subnets. The list is periodically updated from an external server and stored in text file format on an external server. After the FortiGate imports this list, it can be used as a source or destination in firewall policies, proxy policies, local-in policies, and ZTNA rules. It can also be used as an external IP block list in DNS filter profiles.

Text file example:

```
192.168.2.100
172.200.1.4/16
172.16.1.2/24
172.16.8.1-172.16.8.100
2001:0db8::eade:27ff:fe04:9a01/120
2001:0db8::eade:27ff:fe04:aa01-2001:0db8::eade:27ff:fe04:ab01
```


The file contains one IPv4 or IPv6 address, address range, or subnet per line. See [External resources file format](https://docs.fortinet.com/document/fortigate/7.2.4/administration-guide/009463/threat-feeds#format) for more information about the IP list formatting style.

Example configuration
---------------------

In this example, a list of destination IP addresses is imported using the IP address threat feed. The newly created threat feed is then used as a destination in a firewall policy with the action set to deny. Any traffic that passes through the FortiGate and matches the defined firewall policy will be dropped.

###### To configure an IP address threat feed in the GUI:

1.  Go to _Security Fabric > External Connectors_ and click _Create New_.
2.  In the _Threat Feeds_ section, click _IP Address_.
3.  Set the _Name_ to _IPEX\_IP\_Blocklist_.
4.  Set the _Update method_ to _External Feed_.
5.  Set the _URI of external resource_ to _https://raw.githubusercontent.com/ZEROF/ipextractor/main/ipexdbl.txt_.
6.  Configure the remaining settings as required, then click _OK_.
7.  Edit the connector, then click _View Entries_ to view the IP addresses in the feed.
    
    ![](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/resources/541164a8-66d4-11ed-96f0-fa163e15d75b/images/ae89566b98e361cc8acd21b04fb21b97_724-IP%20address%20feed.png)
    

###### To configure an IP address threat feed in the CLI:

```
config system external-resource
   edit "IPEX_IP_Blocklist"
      set type address
      set resource "https://raw.githubusercontent.com/ZEROF/ipextractor/main/ipexdbl.txt"
      set server-identity-check {none | basic | full}
   next
end
```




###### To apply an IP address threat feed in a firewall policy:

1.  Go to _Policy & Objects > Firewall Policy_ and create a new policy, or edit an existing one.
    
2.  Configure the policy fields as required.
    
3.  In the _Destination_ field, click the _+_ and select _IPEX\_IP\_Blocklist_ from the list (in the _IP ADDRESS FEED_ section).
    
4.  Set _Action_ to _DENY_.
    
5.  Enable _Log Allowed Traffic_.
    
6.  Click _OK_.
    

Applying an IP address threat feed as an external IP block list in a DNS filter profile
---------------------------------------------------------------------------------------

An IP address threat feed can be applied by enabling _External IP Block Lists_ in a DNS filter profile. Any DNS query that passes through the FortiGate and resolves to any of the IP addresses in the threat feed list will be dropped.

###### To configure the DNS filter profile:

1.  Go to _Security Profiles > DNS Filter_ and create a new profile, or edit an existing one.
    
2.  Enable _External IP Block Lists_.
3.  Click the _+_ and select _IPEX\_IP\_Blocklist_ from the list.
4.  Click _OK_.
    

###### To apply the DNS filter profile in a firewall policy:

1.  Go to _Policy & Objects > Firewall Policy_ and create a new policy, or edit an existing one.
    
2.  Configure the policy fields as required.
    
3.  Under _Security Profiles_, enable _DNS Filter_ and select the profile used in the previous procedure.
    
4.  Enable _Log Allowed Traffic_.
    
5.  Click _OK_.
    

IP addresses that match the IP address threat feed list will be blocked.

###### To view the DNS query logs:

1.  Go to _Log & Report > Security Events_ and select _DNS Query_.
    
2.  View the log details in the GUI, or download the log file:
    
```
1: date=2023-02-06 time=15:06:50 eventtime=1675724810452621179 tz="-0800" logid="1501054400" type="utm" subtype="dns" eventtype="dns-response" level="warning" vd="root" policyid=0 sessionid=555999 srcip=172.20.120.13 srcport=59602 srccountry="Reserved" srcintf="port2" srcintfrole="undefined" dstip=172.20.120.12 dstport=53 dstcountry="Reserved" dstintf="root" dstintfrole="undefined" proto=17 profile="default" xid=24532 qname="dns.google" qtype="A" qtypeval=1 qclass="IN" ipaddr="208.91.112.55" msg="Domain was blocked because it is in the domain-filter list" action="redirect" domainfilteridx=0 domainfilterlist="IPEX_IP_Blocklist"
```

    

Applying an IP address threat feed in a local-in policy
-------------------------------------------------------

An IP address threat feed can be applied as a source or destination in a local-in policy.

In this example, a previously created IP address threat feed named IPEX_IP_Blocklist is used as a source address in a local-in-policy. Any traffic originating from any of the IP addresses in the threat feed list and destined for the FortiGate will be dropped.

###### To apply an IP address threat feed in a local-in policy:

```
config firewall local-in-policy
    edit 1
        set intf "any"
        set srcaddr "IPEX_IP_Blocklist"
        set dstaddr "all"
        set service "ALL"
        set schedule "always"
    next
end
```


###### To test the configuration:

1.  From one of the IP addresses listed in IP address threat feed (in this case 172.16.200.2), start a continuous ping to port1:
    
```
ping 172.16.200.1 –t
```

    
2.  On the FortiGate, enable debug flow:
    
```
# diagnose debug flow filter addr 172.16.200.2
# diagnose debug flow filter proto 1
# diagnose debug enable
# diagnose debug flow trace start 10
```

    
3.  The output of the debug flow shows that traffic is dropped by local-in policy 1:
    
```
id=65308 trace_id=11 func=print_pkt_detail line=5939 msg="vd-root:0 received a packet(proto=1, 172.16.200.2:0->172.16.200.1:2048) tun_id=0.0.0.0 from port1. type=8, code=0, id=0, seq=0."
id=65308 trace_id=11 func=init_ip_session_common line=6121 msg="allocate a new session-0002f318, tun_id=0.0.0.0"
id=65308 trace_id=11 func=__vf_ip_route_input_rcu line=2012 msg="find a route: flag=80000000 gw-0.0.0.0 via root"
id=65308 trace_id=11 func=fw_local_in_handler line=545 msg="iprope_in_check() check failed on policy 1, drop"
```
