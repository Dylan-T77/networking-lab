# Network Reference

A practical reference for core networking concepts encountered during Project 002.

This document is intentionally vendor-neutral. It records concepts and behaviour that can be reused throughout the lab rather than documenting a specific device.

## 1. IPv4 and IPv6

### IPv4

IPv4 uses 32-bit addresses, commonly written in dotted-decimal notation:

```text
192.168.0.10
```

Private IPv4 address ranges commonly used in internal networks include:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

### IPv6

IPv6 uses 128-bit addresses and provides a vastly larger address space than IPv4.

IPv6 can provide globally routable addresses to hosts, so IPv6 firewall policy remains important even though traditional IPv4 NAT is not required in the same way.

---

## 2. NAT

**NAT (Network Address Translation)** translates between addresses used on different network boundaries.

A common home-network arrangement is:

```text
Internet
   |
Public IP
   |
Router / NAT
   |
192.168.0.0/24
   |
+--+---------+---------+
|            |         |
PC           Pi        Phone
```

NAT commonly allows many private hosts to share one public IPv4 address.

NAT should not be treated as a replacement for a firewall. Security policy should be enforced explicitly.

---

## 3. Port Forwarding

Port forwarding creates a static mapping from an inbound port to a specific internal host and port.

Example:

```text
Public TCP 443 -> 192.168.0.20:443
```

Use port forwarding only when an externally reachable service is actually required. Minimize exposed ports and secure the destination service.

---

## 4. Port Triggering

Port triggering creates temporary inbound mappings after a device initiates traffic matching a configured trigger.

It can support older applications that require dynamic inbound connections, but it is not normally necessary for a basic modern network.

---

## 5. UPnP

**UPnP (Universal Plug and Play)** can allow devices on a trusted LAN to request automatic NAT/port mappings from the gateway.

Advantages:

- Convenient for applications and games
- Reduces manual configuration

Risks:

- Applications can create mappings without manual approval
- A compromised internal device may abuse automatic port mapping

For controlled lab environments, disabling UPnP is often preferable unless a test specifically requires it.

---

## 6. DMZ

A router's consumer DMZ feature commonly forwards unsolicited inbound traffic to a designated internal host.

It should not be confused with a properly segmented enterprise DMZ network.

Avoid using a host DMZ as a shortcut for port forwarding. Explicitly forwarding only the required ports provides much tighter control.

---

## 7. DHCP

**DHCP (Dynamic Host Configuration Protocol)** automatically provides network configuration to clients.

Typical DHCP information includes:

- IP address
- Subnet mask/prefix
- Default gateway
- DNS servers
- Lease duration

A network should normally have one authoritative DHCP service for a given broadcast domain. Accidentally running multiple DHCP servers can produce inconsistent addressing and connectivity failures.

### Reservations

A DHCP reservation associates a device identifier, commonly a MAC address, with a preferred IP address.

Reservations are useful for infrastructure such as servers, network appliances and lab systems that need predictable addresses while remaining under DHCP management.

---

## 8. IP and MAC Binding

IP/MAC binding associates an IP address with a specific MAC address and, depending on the implementation, can enforce or validate that relationship at the local network level.

This can help with predictable addressing and some ARP-related protections, but it is not a complete network-security mechanism.

Modern client devices may use randomized/private MAC addresses, so bindings should be created deliberately.

---

## 9. VLANs

**VLAN (Virtual Local Area Network)** provides logical network segmentation over shared physical infrastructure.

A VLAN can separate traffic into different broadcast domains, for example:

```text
VLAN 10  Management
VLAN 20  Clients
VLAN 30  Servers
VLAN 40  Guest
```

Inter-VLAN communication requires routing and should be controlled by appropriate firewall or access-control policy.

---

## 10. Routing

Routing determines where packets should be forwarded based on their destination network.

A routing table may contain entries such as:

```text
Destination       Gateway        Interface
192.168.10.0/24   10.0.0.2       LAN
10.0.0.0/24       connected      LAN
0.0.0.0/0         ISP gateway    WAN
```

The default route (`0.0.0.0/0` in IPv4) is used when no more specific route matches.

---

## 11. ALG

**ALG (Application Layer Gateway)** is a protocol-specific NAT helper. It can inspect or modify application traffic so certain protocols function through NAT.

Common examples include helpers for:

- FTP
- TFTP
- RTSP
- H.323
- SIP

ALG settings are implementation-specific. A protocol helper being enabled does not mean the router is running that application server.

SIP ALG in particular can interfere with some VoIP deployments, so it should be evaluated against the actual environment rather than changed blindly.

---

## 12. VPN Passthrough

VPN passthrough features help particular VPN protocols traverse NAT.

Common examples include:

- PPTP passthrough
- L2TP passthrough
- IPsec passthrough

Passthrough is different from running a VPN server on the router.

PPTP is obsolete and should not be selected for new VPN deployments. Modern VPN designs should use stronger protocols such as WireGuard or appropriately configured IPsec/IKEv2.

---

## 13. CWMP / TR-069

**CWMP (CPE WAN Management Protocol)**, commonly associated with TR-069, allows a managed customer-premises device to communicate with an **ACS (Auto Configuration Server)** for remote provisioning and management.

Potential functions include:

- Configuration provisioning
- Diagnostics
- Status reporting
- Firmware management

A device's CWMP credentials are separate from its normal local administration credentials. The presence of a stored CWMP username/password does not by itself mean remote management is active.

Periodic Inform is used by a CWMP client to periodically initiate communication with its ACS when CWMP is operational.

---

## 14. Remote Management

Remote administration of network equipment should be treated separately from normal outbound internet connectivity.

Security principles:

- Disable WAN-side administration unless required
- Use strong unique administrative credentials
- Prefer encrypted management protocols
- Restrict management sources where possible
- Keep firmware current
- Audit exposed services and ports

---

## 15. Practical Security Baseline

For a small controlled network:

```text
NAT                    Enabled where required
DHCP                   One authoritative server per LAN
UPnP                   Disabled unless required
DMZ                    Disabled unless specifically justified
Port forwarding        None unless a service requires it
Port triggering        None unless required
Remote management     Disabled unless required
Firewall               Enabled
IPv6 firewall          Enabled when IPv6 is in use
Admin credentials      Strong and unique
Firmware               Maintained through supported update methods
```

The objective is not to disable every feature. The objective is to keep the network's attack surface intentional and understandable.

---

## 16. Lab Principle

Reference knowledge is not evidence of implementation.

A concept becomes a completed lab result only after it has been configured, tested and documented in the Project 002 environment.
