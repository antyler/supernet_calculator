# supernet_calculator
This script calculates the subnet CIDR block(IP's) based on the number of servers of a particular type needed i.e Database(Exadata, IaaS), Middle Tier, Private Load balancer, Public load balancer, OTD servers and finally creates the supernet 
Step by step it will ask the number of IPs needed for any particular server type and accrodingly it will take a buffer of 15/20% as cases of future expansions needs to be considered.
It then calculates individual subnet size and gives the supernet block size.

NOTE: Its customized as per company requirements and can be tweaked accordingly.
