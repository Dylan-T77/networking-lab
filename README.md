# Networking Lab

**Project:** 002  
**Status:** Complete / Documented

A hands-on networking laboratory for learning, testing, breaking and troubleshooting core network infrastructure.

Project 001 established the Windows infrastructure foundation. Project 002 moved outward into the network itself: addressing, services, routing, segmentation, security, traffic analysis and troubleshooting.

## Objectives

- Understand TCP/IP and subnetting in practice
- Build and troubleshoot DNS and DHCP services
- Explore IPv4 and IPv6 behaviour
- Understand NAT and controlled inbound connectivity
- Explore routing, switching and VLANs
- Configure and test firewall behaviour
- Capture and analyse network traffic
- Investigate network failures systematically
- Document working configurations and failure states
- Build a reusable networking reference

## Completed Scope

### Foundations

- [x] OSI and TCP/IP models
- [x] Ethernet and MAC addressing
- [x] IPv4 addressing and subnetting
- [x] IPv6 fundamentals
- [x] ARP and neighbour discovery

### Network Services

- [x] DHCP
- [x] DNS
- [x] Name resolution troubleshooting
- [x] DHCP reservations and addressing strategy

### Network Infrastructure

- [x] NAT
- [x] Port forwarding analysis
- [x] Routing and static routes
- [x] VLANs
- [x] Inter-VLAN routing

### Security

- [x] Firewall rules
- [x] Network segmentation
- [x] Access control
- [x] Remote management security
- [x] Service exposure and attack surface

### Traffic Analysis

- [x] Packet-flow analysis
- [x] TCP/UDP behaviour
- [x] DNS traffic analysis
- [x] DHCP traffic analysis
- [x] Troubleshooting with packet evidence

### Troubleshooting

- [x] Addressing failures
- [x] DHCP failures
- [x] DNS failures
- [x] Routing failures
- [x] Firewall failures
- [x] Connectivity diagnostics
- [x] Documented failure scenarios

## Project Structure

```text
networking-lab/
├── README.md
├── docs/
│   ├── addressing.md
│   ├── services.md
│   ├── routing-and-vlans.md
│   ├── security.md
│   ├── troubleshooting.md
│   └── lab-results.md
├── labs/
│   └── subnet-calculator.py
└── reference/
    └── network-reference.md
```

## Method

**Build → test → break → investigate → fix → document.**

The project includes addressing calculations, service tests, segmentation tests, security checks and deliberate failure scenarios. Results and limitations are documented rather than treating reference material as evidence of implementation.

## Outcome

Project 002 established a complete vendor-neutral networking workflow on top of the Windows infrastructure from Project 001. The main outcome is a repeatable approach to network design and fault isolation, with configuration logic and expected behaviour documented for future labs.

## Project Status

**PROJECT_001 - Windows Infrastructure Lab:** Complete / Documented  
**PROJECT_002 - Networking Lab:** Complete / Documented  
**PROJECT_003 - PowerShell IT Toolkit:** Active / Building