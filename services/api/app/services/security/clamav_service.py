"""Minimal ClamAV client (clamd INSTREAM protocol) using only the standard library.

Scans uploaded file bytes for malware before the app processes them. Designed to be
safe-by-default: if scanning is disabled it is a no-op; if the scanner is unreachable the
behaviour is governed by MALWARE_SCAN_FAIL_CLOSED.
"""
from __future__ import annotations

import logging
import socket
import struct
from dataclasses import dataclass

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

_CHUNK = 8192


class ScannerUnavailable(Exception):
    pass


@dataclass
class ScanResult:
    clean: bool
    signature: str | None = None  # set when a threat is found


def _instream(sock: socket.socket, data: bytes) -> str:
    sock.sendall(b'nINSTREAM\n')
    view = memoryview(data)
    for i in range(0, len(data), _CHUNK):
        chunk = view[i:i + _CHUNK]
        sock.sendall(struct.pack('!L', len(chunk)) + chunk)
    sock.sendall(struct.pack('!L', 0))  # zero-length chunk = end of stream
    resp = b''
    while True:
        part = sock.recv(4096)
        if not part:
            break
        resp += part
        if resp.endswith(b'\n'):
            break
    return resp.decode('utf-8', 'replace').strip()


def scan_bytes(data: bytes) -> ScanResult:
    """Scan bytes with clamd. Raises ScannerUnavailable if the daemon can't be reached."""
    try:
        with socket.create_connection((settings.clamav_host, settings.clamav_port),
                                      timeout=settings.clamav_timeout_seconds) as sock:
            sock.settimeout(settings.clamav_timeout_seconds)
            reply = _instream(sock, data)
    except OSError as exc:
        raise ScannerUnavailable(str(exc)) from exc
    # Examples: "stream: OK"  |  "stream: Eicar-Test-Signature FOUND"
    if reply.endswith('OK'):
        return ScanResult(clean=True)
    if 'FOUND' in reply:
        sig = reply.split(':', 1)[-1].strip().removesuffix(' FOUND').strip()
        return ScanResult(clean=False, signature=sig or 'unknown')
    # ERROR or unexpected -> treat as unavailable
    raise ScannerUnavailable(reply or 'empty response')


def ping() -> dict:
    """Return scanner reachability/version for the admin dashboard."""
    if not settings.malware_scan_enabled:
        return {'enabled': False, 'reachable': False, 'version': None}
    try:
        with socket.create_connection((settings.clamav_host, settings.clamav_port),
                                      timeout=settings.clamav_timeout_seconds) as sock:
            sock.sendall(b'nVERSION\n')
            version = sock.recv(4096).decode('utf-8', 'replace').strip()
        return {'enabled': True, 'reachable': True, 'version': version}
    except OSError as exc:
        return {'enabled': True, 'reachable': False, 'version': None, 'error': str(exc)}
