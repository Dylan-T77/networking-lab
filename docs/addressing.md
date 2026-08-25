# Addressing and Subnetting Lab

## Objective

Validate IPv4 addressing, subnet boundaries, host capacity and a repeatable addressing plan for the lab.

## Test network

`10.10.0.0/16` was divided into `/24` VLAN networks.

For a `/24`:

- Prefix length: 24 bits
- Host bits: 8
- Total addresses: `2^8 = 256`
- Usable hosts: `256 - 2 = 254`
- Mask: `255.255.255.0`

## VLAN allocation

| VLAN | Network | First host | Last host | Broadcast |
|---:|---|---|---|---|
| 10 | 10.10.10.0/24 | 10.10.10.1 | 10.10.10.254 | 10.10.10.255 |
| 20 | 10.10.20.0/24 | 10.10.20.1 | 10.10.20.254 | 10.10.20.255 |
| 30 | 10.10.30.0/24 | 10.10.30.1 | 10.10.30.254 | 10.10.30.255 |
| 40 | 10.10.40.0/24 | 10.10.40.1 | 10.10.40.254 | 10.10.40.255 |

## Verification

The network address and broadcast address were excluded from host assignment. Gateway `.1` was reserved on each VLAN and DHCP pools were placed away from infrastructure reservations.

## Result

**PASS.** The addressing plan provides clear broadcast-domain separation, predictable gateways and sufficient host capacity for the intended lab population.
