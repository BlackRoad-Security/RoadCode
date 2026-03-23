# RoadCode

> Canonical RoadCode workspace and automation hub for BlackRoad-Security.

Part of the [BlackRoad OS](https://blackroad.io) ecosystem — [BlackRoad-Security](https://github.com/BlackRoad-Security)

---

# BlackRoad-Security — RoadCode

> Security & Compliance division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Security auditing, penetration testing, compliance checks, threat detection, and fleet hardening. Every node in the BlackRoad fleet gets scanned, every agent gets verified, every connection gets audited.

## Capabilities

| Area | What We Do |
|------|-----------|
| **Cipher Agent** | Automated security scanning across the 7-node fleet |
| **Penetration Testing** | Network + application pen tests against all services |
| **Compliance Checks** | License auditing, secret detection, dependency scanning |
| **Fleet Hardening** | SSH key rotation, firewall rules, WireGuard mesh verification |
| **RoadBlock** | Intrusion detection + automatic lockdown |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Security (Security & Compliance)
      ├── RoadCode              ← this repo (workspace + automation)
      ├── penetration-testing    ← pen test suites + reports
      ├── security-audits        ← audit logs + compliance records
      ├── roadblock              ← intrusion detection system
      ├── operator               ← CLI tools + security scripts
      └── source                 ← canonical source tree
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-Security/RoadCode) — Workspace hub (this repo)
- [`penetration-testing`](https://github.com/BlackRoad-Security/penetration-testing) — Pen test tooling + reports
- [`security-audits`](https://github.com/BlackRoad-Security/security-audits) — Audit records + compliance
- [`roadblock`](https://github.com/BlackRoad-Security/roadblock) — Intrusion detection
- [`operator`](https://github.com/BlackRoad-Security/operator) — CLI + security automation

## Fleet Security Overview

- **WireGuard mesh**: 12/12 SSH connections verified across all nodes
- **Tor hidden services**: 3 Pi nodes reachable via .onion addresses
- **Gitea**: Primary git host on Octavia — all repos scanned for secrets
- **Memory security**: Agent identity verification + audit trails via `memory-security.sh`
- **Start Certification**: 5 real check scripts, 80% pass rate on operator

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — physical node security
- **Cloud**: [BlackRoad-Cloud](https://github.com/BlackRoad-Cloud) — edge + TLS via Caddy on Gematria

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
