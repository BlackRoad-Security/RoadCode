"""Port scanner for fleet security audits."""
import asyncio
import socket
from dataclasses import dataclass

@dataclass
class ScanResult:
    host: str
    port: int
    open: bool
    service: str = ""
    banner: str = ""

COMMON_PORTS = {
    22: "ssh", 80: "http", 443: "https", 3000: "grafana",
    3100: "gitea", 5432: "postgresql", 6333: "qdrant",
    6379: "redis", 8080: "http-alt", 8094: "roundtrip",
    8883: "mqtt-tls", 9090: "prometheus", 11434: "ollama",
}

async def scan_port(host: str, port: int, timeout: float = 2.0) -> ScanResult:
    try:
        _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return ScanResult(host, port, True, COMMON_PORTS.get(port, "unknown"))
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return ScanResult(host, port, False)

async def scan_fleet(hosts: list[str], ports: list[int] | None = None) -> list[ScanResult]:
    ports = ports or list(COMMON_PORTS.keys())
    tasks = [scan_port(h, p) for h in hosts for p in ports]
    return await asyncio.gather(*tasks)
