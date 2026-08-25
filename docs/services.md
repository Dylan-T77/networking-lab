# Network Services Lab

## DHCP

The lab uses one authoritative DHCP scope per VLAN.

### Verification sequence

1. Client requests a lease.
2. DHCP server offers an address from the correct scope.
3. Client requests the offered address.
4. Server acknowledges the lease.
5. Client receives gateway and DNS settings.
6. Client verifies local and routed connectivity.

**Result: PASS.** Addressing remains within the intended VLAN scope and infrastructure reservations are separated from dynamic pools.

## DNS

The DNS test separates transport from name resolution.

### Verification sequence

```text
ping gateway
↓
reach DNS server by IP
↓
query DNS record
↓
resolve application hostname
```

A successful IP path with a failed hostname lookup indicates a DNS-layer problem rather than a general connectivity failure.

**Result: PASS.** The troubleshooting sequence correctly isolates DNS failures from routing and Layer-2 failures.

## Failure test

A DNS server outage was modelled. Raw IP connectivity remained available while hostname resolution failed. Restoring DNS availability restored normal name resolution without changing the client address or gateway.

## Outcome

DHCP provides controlled addressing while DNS provides service discovery. Testing them as separate layers makes faults easier to isolate and prevents application symptoms from being mistaken for physical or routing failures.
