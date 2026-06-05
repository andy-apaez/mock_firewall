# Mock Firewall

A minimal Python simulation of how a firewall evaluates incoming traffic against a ruleset.

---

## What the Code Does

The program simulates packets arriving at a firewall. Each packet is a randomly generated IP address checked against a static ruleset — if the IP matches a blocked entry, it's `DENY`ed; otherwise it defaults to `ALLOW`.

- `generate_random_ip()` — Generates a random IPv4 address to simulate incoming traffic.
- `mock_firewall_rules(ip, rule)` — Iterates the ruleset dictionary and returns the matching action, defaulting to `ALLOW`.
- `main()` — Runs 10 simulated packets through the firewall and prints each result.

The default-allow policy means unknown traffic passes unless explicitly blocked — the opposite of what sensitive systems use.

---

## Concepts Being Explored

**Default-Allow vs. Default-Deny** — This code allows anything not explicitly blocked. Real secure systems flip this: block everything, allow only what's known safe.

**Linear Rule Lookup** — `mock_firewall_rules` loops through every rule, making it O(n). Real firewalls use hash tables or TCAM hardware to match rules in near-constant time across millions of entries.

**Stateless Filtering** — Each packet is evaluated in isolation with no memory of past traffic. Modern stateful firewalls track TCP connection state so they can distinguish established sessions from unsolicited probes.

---

## Potential Weaknesses

| Weakness | Description |
|---|---|
| **IP spoofing** | Attackers can forge source IPs to bypass the blocklist. |
| **No port/protocol awareness** | Threats are often port-specific; this ruleset ignores that entirely. |
| **Blocklist-only** | Any unknown attacker IP passes through by default. |
| **No logging** | Denied packets aren't stored — no audit trail or alerting. |

---

## How Real Firewalls Build on This

The dictionary lookup here is the conceptual core of every firewall: *match a packet attribute against a ruleset, return a verdict*. Production systems layer on top:

1. **Richer rules** — Match on source/destination IP, port, and protocol simultaneously.
2. **Ordered rule chains** — First match wins, as in `iptables`/`nftables`.
3. **Connection tracking** — A state table auto-permits return traffic without explicit rules.
4. **Deep packet inspection** — NGFWs inspect payload content for malware signatures.
5. **Hardware acceleration** — ASICs/FPGAs handle rule matching at 100 Gbps+ line rate.
