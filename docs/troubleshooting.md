# Networking Troubleshooting Lab

## Method

The troubleshooting workflow is deliberately layered:

```text
Physical / link
↓
Addressing
↓
ARP / neighbour discovery
↓
Gateway
↓
Routing
↓
Firewall / ACL
↓
DNS
↓
Transport
↓
Application
```

## Test matrix

| Failure introduced | Observable symptom | Isolation method | Result |
|---|---|---|---|
| Wrong IP/mask | Local and routed failures | Inspect address/prefix | PASS |
| Wrong gateway | Local works, remote fails | Test gateway and route | PASS |
| DHCP unavailable | Missing/incorrect lease | Check lease state and DHCP exchange | PASS |
| DNS unavailable | IP works, hostname fails | Query DNS directly | PASS |
| Firewall deny | Specific service fails | Compare path and policy | PASS |
| Wrong route | Remote subnet unreachable | Inspect routing table | PASS |

## Connectivity diagnostics

The test sequence uses simple tools before deeper packet analysis:

```text
ipconfig /all / ip addr
ping gateway
ping remote IP
tracert / traceroute
nslookup / Resolve-DnsName
Test-NetConnection
arp / ip neigh
```

The objective is to identify the first layer where expected behaviour stops rather than repeatedly testing the application.

## Packet evidence

When configuration checks are inconclusive, packet capture is used to answer questions such as:

- Did the client transmit the request?
- Did the expected server respond?
- Was the response routed back?
- Was DNS actually queried?
- Did the TCP handshake complete?

## Outcome

The failure scenarios demonstrate that network troubleshooting is primarily an isolation problem. A controlled failure is useful because the expected evidence is known in advance and can be compared with the broken state.
