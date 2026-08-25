# Routing and VLAN Lab

## Objective

Separate broadcast domains while retaining controlled Layer-3 communication between required segments.

## VLANs

```text
VLAN 10  Management  10.10.10.0/24
VLAN 20  Clients     10.10.20.0/24
VLAN 30  Servers     10.10.30.0/24
VLAN 40  Guest       10.10.40.0/24
```

Each VLAN has its own gateway at `.1`.

## Routing test

A client on VLAN 20 was required to reach an authorised service on VLAN 30. The expected path is:

```text
Client → VLAN 20 gateway → routing decision → VLAN 30 gateway/interface → Server
```

**Result: PASS.** Authorised inter-VLAN traffic reaches the destination service.

## Segmentation test

Guest traffic was tested against internal destinations. The firewall policy denied Guest → Management and Guest → Servers while allowing Guest → Internet.

**Result: PASS.** Segmentation remains effective at Layer 3 rather than relying only on physical separation.

## Static routing

The routing model was checked for connected networks and a default route. More-specific internal routes take precedence over the default route.

## Outcome

The lab demonstrates the distinction between switching/broadcast domains and routing. VLANs provide separation; routing provides controlled connectivity; firewall policy determines which routed flows are actually allowed.
