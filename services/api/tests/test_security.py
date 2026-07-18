"""Upload malware-scan guard behaviour (scanner mocked; no clamd needed)."""
import pytest
from fastapi import HTTPException

from app.services.security import upload_guard
from app.services.security.clamav_service import ScanResult, ScannerUnavailable


def test_disabled_is_noop(monkeypatch):
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_enabled', False)
    upload_guard.scan_upload_or_raise(b'anything', 'x.txt')  # no raise


def test_clean_passes(monkeypatch):
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_enabled', True)
    monkeypatch.setattr(upload_guard, 'scan_bytes', lambda data: ScanResult(clean=True))
    upload_guard.scan_upload_or_raise(b'hello', 'x.txt')  # no raise


def test_infected_rejected(monkeypatch):
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_enabled', True)
    monkeypatch.setattr(upload_guard, 'scan_bytes', lambda data: ScanResult(clean=False, signature='Eicar-Test-Signature'))
    with pytest.raises(HTTPException) as e:
        upload_guard.scan_upload_or_raise(b'virus', 'x.exe')
    assert e.value.status_code == 422


def test_unavailable_fail_open(monkeypatch):
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_enabled', True)
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_fail_closed', False)
    def boom(data): raise ScannerUnavailable('down')
    monkeypatch.setattr(upload_guard, 'scan_bytes', boom)
    upload_guard.scan_upload_or_raise(b'data', 'x.txt')  # allowed, no raise


def test_unavailable_fail_closed(monkeypatch):
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_enabled', True)
    monkeypatch.setattr(upload_guard.settings, 'malware_scan_fail_closed', True)
    def boom(data): raise ScannerUnavailable('down')
    monkeypatch.setattr(upload_guard, 'scan_bytes', boom)
    with pytest.raises(HTTPException) as e:
        upload_guard.scan_upload_or_raise(b'data', 'x.txt')
    assert e.value.status_code == 503
