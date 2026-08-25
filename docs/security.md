# Network Security Lab

## Baseline

The security model follows least exposure rather than assuming that NAT itself provides security.

### Baseline controls

- Stateful firewall enabled
- WAN administration disabled unless required
- No unnecessary port forwards
- No consumer DMZ shortcut
- UPnP disabled for the controlled lab baseline
- Guest network isolated from internal networks
- Management access restricted to the management segment
- IPv6 filtering considered whenever IPv6 is enabled

## Exposure test

Expected inbound behaviour:

```text
WAN → unsolicited internal connection = DENY
WAN → explicitly required service = ALLOW only when configured
LAN → Internet = ALLOW according to policy
Guest → internal = DENY
```

**Result: PASS.** The baseline follows an explicit-deny approach for unsolicited inbound traffic and isolates guest access.

## Attack-surface review

Potential exposure was evaluated by service rather than by port number alone. A port is only considered acceptable when a corresponding service exists, is required and is appropriately secured.

## Remote management

Remote administration was treated as a separate security decision from ordinary outbound Internet access. Management access is restricted to authorised internal sources.

## Outcome

The security portion of Project 002 established a practical baseline: minimise exposure, segment trust zones and make exceptions explicit. The result is easier to audit and troubleshoot than a network relying on implicit behaviour.
