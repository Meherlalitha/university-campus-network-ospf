**University Campus Network – OSPFv2 Implementation (Cisco Packet Tracer)**

A fully designed, configured, and validated multi‑router campus network built in Cisco Packet Tracer.

This project demonstrates practical networking skills including routing design, OSPFv2 implementation, IP addressing, troubleshooting, and end‑to‑end connectivity validation across multiple LAN environments.



**Project Overview**

This simulation models a realistic university‑style campus network with:

\- A Core Router providing central routing and inter‑LAN connectivity

\- Multiple Distribution Routers serving Academic, Admin, and Server networks

\- Layer‑3 routing using OSPFv2 (Area 0)

\- Structured IP addressing using /24 LANs and /30 point‑to‑point links

\- Full end‑to‑end reachability validated using industry‑standard commands

This project highlights both network design and hands‑on troubleshooting, reflecting real‑world engineering workflows.



**Network Topology:**



\[Campus network topology](diagrams/topology.png)



 **Architecture \& Addressing**

LAN Subnets

|     Network      |   Purpose     |   Gateway    | 

| 192.168.100.0/24 | Academic LAN  |192.168.100.11| 

| 192.168.20.0/24  | Admin LAN     | 192.168.20.1 | 

| 192.168.30.0/24  | Server LAN    | 192.168.30.1 | 



**Router Interconnects**

\- Point‑to‑point transit links using 10.10.10.x/30

\- All routers participate in OSPF Area 0

\- Router IDs assigned for clarity (e.g., 3.3.3.3, 6.6.6.6)



 **Key Features**

\- Dynamic Routing with OSPFv2

All LAN and transit networks are advertised and learned dynamically.

\- Layered Network Design

Core → Distribution → Access hierarchy modeled after enterprise/campus networks.

\- Full End‑to‑End Connectivity

Verified using ping, traceroute, and routing table inspection.

\- Troubleshooting \& Diagnostics

Includes real debugging of missing OSPF advertisements and unreachable networks.

\- Professional Documentation

Complete configs, diagrams, and validation outputs included in the repository.



**Validation \& Testing**

Connectivity and routing were verified using:

\- show ip ospf neighbor

\- show ip route ospf

\- show ip route <network>

\- ping <destination>

\- traceroute <destination>

Example validation:

\- Successful traceroute from Core → Academic LAN host (192.168.100.14)

\- OSPF routes correctly learned for all LANs

\- All inter‑LAN communication confirmed

Full validation logs are available in:

validation/verification.txt



**Configuration Files**

All router configurations are included for transparency and reproducibility:

configs/

├─ core-router.txt

├─ serv-r3.txt

├─ serv-r6.txt

├─ acd-r4.txt

└─ admin-r1.txt







**Repository Structure**

university-campus-network-ospf/

├─ README.md

├─ packet-tracer/

│  └─ university-campus-network-ospf-meher.pkt

├─ configs/

├─ diagrams/

├─ validation/

└─ project-report/



**Project Story (What I Solved)**

This project began as a multi‑LAN campus design, but early testing revealed routing gaps — specifically, the Server LAN (192.168.30.0/24) was missing from the Core router’s routing table.

Through systematic troubleshooting, I:

\- Inspected OSPF neighbors and LSAs

\- Identified missing OSPF network statements on Serv‑R6

\- Corrected advertisements to include the Server LAN

\- Verified propagation to Serv‑R3 and the Core

\- Confirmed full reachability using traceroute and ping

This reflects real‑world network engineering: diagnosing incomplete routing tables, validating control‑plane behavior, and confirming data‑plane connectivity.



**How to Use This Project**

\- Open the .pkt file in Cisco Packet Tracer

\- Power on all devices

\- Allow OSPF to converge

\- Run validation commands from the Core router:

\- show ip ospf neighbor

\- show ip route ospf

\- ping 192.168.30.10

\- traceroute 192.168.100.14



**Why This Project Matters**

This repository demonstrates:

\- Practical routing knowledge

\- Ability to debug real network issues

\- Clear documentation and professional presentation

\- Hands‑on experience with Cisco IOS

\- Understanding of enterprise‑style network design









