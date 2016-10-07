Monitor your haproxy cluster using zenoss and snmp

You'll need to configure haproxy to use socket for stats[1], and your snmpd to run a perl script[2] to read from that socket (trust me this is pretty easy). You'll also likely need to update the PythonCollector ZenPack and install the CalculatedPerformance ZenPack.

[1] http://serverfault.com/questions/273820/haproxy-perl-plugin-and-net-snmpd-on-ubuntu-10-04

[2] http://www.haproxy.org/download/contrib/netsnmp-perl/haproxy.pl

note: this is adapted for the community from another proprietary version I had written. I have not actually tested this in production. but... it should work. Please test and submit issues or pull requests.



