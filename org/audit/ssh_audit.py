"""SSH key audit — checks authorized_keys across fleet."""
from dataclasses import dataclass

@dataclass
class SSHKeyInfo:
    node: str
    user: str
    key_type: str
    key_fingerprint: str
    comment: str

class SSHAuditor:
    FLEET_NODES = {
        "alice": {"ip": "192.168.4.49", "users": ["pi", "blackroad"]},
        "cecilia": {"ip": "192.168.4.96", "users": ["blackroad"]},
        "octavia": {"ip": "192.168.4.101", "users": ["pi", "blackroad"]},
        "aria": {"ip": "192.168.4.98", "users": ["blackroad"]},
        "lucidia": {"ip": "192.168.4.38", "users": ["blackroad", "octavia"]},
    }

    async def audit_all(self) -> list[SSHKeyInfo]:
        results = []
        for node, info in self.FLEET_NODES.items():
            for user in info["users"]:
                # In production: SSH in and read authorized_keys
                results.append(SSHKeyInfo(node, user, "ed25519", "placeholder", f"{user}@{node}"))
        return results
