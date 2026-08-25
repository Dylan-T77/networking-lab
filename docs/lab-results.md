# Project 002 - Networking Lab Results

**Status:** Complete  
**Project:** 002  
**Method:** Build → test → break → investigate → fix → document

## 1. Lab topology

The lab was designed as four logical segments behind a router/firewall:

```text
                         WAN / Internet
                              |
                       [ Router / FW ]
                              |
        +---------------------+---------------------+
        |                     |                     |
   VLAN 10                VLAN 20               VLAN 30
 Management               Clients                Servers
 10.10.10.0/24           10.10.20.0/24          10.10.30.0/24
        |
   VLAN 40 Guest
   10.10.40.0/24
```

Gateway convention: `.1` on each VLAN. Infrastructure addresses are reserved at the low end of each subnet; dynamic client pools start at `.100`.

## 2. Addressing calculations

| Segment | Network | Usable hosts | Gateway | DHCP pool |
|---|---|---:|---|---|
| Management | 10.10.10.0/24 | 254 | 10.10.10.1 | .100–.199 |
| Clients | 10.10.20.0/24 | 254 | 10.10.20.1 | .100–.229 |
| Servers | 10.10.30.0/24 | 254 | 10.10.30.1 | .100–.149 |
| Guest | 10.10.40.0/24 | 254 | 10.10.40.1 | .100–.249 |

Subnet mask: `255.255.255.0` (`/24`).  
Each segment provides 256 total addresses, 254 usable host addresses, one network address and one broadcast address.

## 3. Service design

### DHCP

One authoritative DHCP scope was defined per VLAN. Reservations were used for infrastructure systems where stable addressing was required.

### DNS

Internal records followed the lab naming convention:

```text
 dc01.corp.lab
 client01.corp.lab
 router.corp.lab
```

The troubleshooting sequence was tested as:

```text
IP connectivity → gateway → DNS server reachability → DNS query → application
```

### NAT

Outbound traffic from the private VLANs is translated at the WAN boundary. No inbound service was exposed unless a specific port-forward requirement existed.

## 4. VLAN and routing design

Inter-VLAN routing was deliberately enabled at the gateway rather than treating VLANs as isolated Layer-2 islands. Firewall policy then controlled which flows were permitted.

Baseline policy:

- Management → all internal segments: permitted for administration
- Clients → Servers: permitted only for required services
- Servers → Clients: restricted
- Guest → internal VLANs: denied
- Guest → Internet: permitted
- WAN → internal: denied by default

## 5. Security tests

| Test | Expected | Result |
|---|---|---|
| Client reaches own gateway | Pass | PASS |
| Client reaches authorised server service | Pass | PASS |
| Guest reaches Internet | Pass | PASS |
| Guest reaches Management VLAN | Block | PASS — blocked |
| Unsolicited WAN connection | Block | PASS — blocked |
| Unapproved inbound port | Block | PASS — blocked |
| Management access from authorised segment | Pass | PASS |

## 6. Failure scenarios

### Scenario A - Wrong subnet mask

A client was modelled with an incorrect mask. The host remained locally configured but could not correctly determine the remote network boundary. Restoring `/24` returned normal routing behaviour.

### Scenario B - Incorrect default gateway

The client retained a valid address but could not reach off-subnet destinations. Gateway correction restored routed connectivity.

### Scenario C - DNS failure

Raw IP connectivity was retained while hostname resolution failed. Testing the DNS server independently separated the name-resolution fault from the underlying network path.

### Scenario D - Firewall denial

A permitted client-to-server flow was deliberately denied. Packet/path testing showed that addressing and routing were intact; restoring the rule returned the service path.

## 7. Traffic-analysis observations

The expected protocol sequence was documented for the major services:

- DHCP: Discover → Offer → Request → Acknowledgement
- DNS: client query → resolver → response
- TCP: SYN → SYN/ACK → ACK before application payload
- ARP/ND: neighbour resolution before local delivery where required

Packet evidence was treated as the source of truth when higher-layer symptoms were ambiguous.

## 8. Test summary

**Addressing:** PASS  
**Subnet calculations:** PASS  
**DHCP design:** PASS  
**DNS troubleshooting workflow:** PASS  
**Routing model:** PASS  
**VLAN segmentation:** PASS  
**Firewall policy:** PASS  
**NAT design:** PASS  
**Failure isolation:** PASS

## 9. Outcome

Project 002 established a complete vendor-neutral network design and troubleshooting workflow on top of the Windows infrastructure from Project 001. The major outcome was not simply a working topology; it was a repeatable method for isolating faults by layer and proving the cause with configuration or packet evidence.

> Note: results in this repository are reproducible lab/design tests. They are not claims about a specific production router or ISP configuration.
