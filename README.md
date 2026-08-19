# Networking Lab

**Project:** 002  
**Status:** Active / Building

A hands-on networking laboratory for learning, testing, breaking and troubleshooting core network infrastructure.

Project 001 established the Windows infrastructure foundation. Project 002 moves outward into the network itself: addressing, services, routing, segmentation, security, traffic analysis and troubleshooting.

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

## Project 002 Scope

### Foundations

- [ ] OSI and TCP/IP models
- [ ] Ethernet and MAC addressing
- [ ] IPv4 addressing and subnetting
- [ ] IPv6 fundamentals
- [ ] ARP and neighbour discovery

### Network Services

- [ ] DHCP
- [ ] DNS
- [ ] Name resolution troubleshooting
- [ ] DHCP reservations and addressing strategy

### Network Infrastructure

- [ ] NAT
- [ ] Port forwarding
- [ ] Routing and static routes
- [ ] VLANs
- [ ] Inter-VLAN routing

### Security

- [ ] Firewall rules
- [ ] Network segmentation
- [ ] Access control
- [ ] Remote management security
- [ ] Service exposure and attack surface

### Traffic Analysis

- [ ] Packet capture
- [ ] TCP/UDP analysis
- [ ] DNS traffic analysis
- [ ] DHCP traffic analysis
- [ ] Troubleshooting with packet evidence

### Troubleshooting

- [ ] Addressing failures
- [ ] DHCP failures
- [ ] DNS failures
- [ ] Routing failures
- [ ] Firewall failures
- [ ] Connectivity diagnostics
- [ ] Documented failure scenarios

## Project Structure

```text
networking-lab/
├── README.md
├── docs/
│   ├── fundamentals.md
│   ├── addressing.md
│   ├── services.md
│   ├── routing-and-vlans.md
│   └── security.md
├── labs/
├── reference/
│   └── network-reference.md
├── diagrams/
└── configs/
```

## Reference

The `reference/` directory contains vendor-neutral networking concepts and reusable technical notes. It is a reference layer, not a record of completed lab work.

## Method

**Build → test → break → investigate → fix → document.**

No implementation is claimed until it has been tested. Planned work, documented procedures and verified results are kept explicitly separate.

## Project Status

**PROJECT_001 — Windows Infrastructure Lab:** Complete / Documented  
**PROJECT_002 — Networking Lab:** Active / Building
