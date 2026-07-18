"""Run pip-audit to check installed Python dependencies against known vulnerabilities.

Invoked on demand from the admin security dashboard. Requires network access to the
vulnerability database (OSV/PyPI). Returns a compact summary.
"""
from __future__ import annotations

import json
import subprocess


def run_pip_audit(timeout: int = 120) -> dict:
    try:
        proc = subprocess.run(
            ['pip-audit', '--format', 'json', '--progress-spinner', 'off'],
            capture_output=True, timeout=timeout, text=True,
        )
    except FileNotFoundError:
        return {'ok': False, 'error': 'pip-audit is not installed in this image.'}
    except subprocess.TimeoutExpired:
        return {'ok': False, 'error': 'pip-audit timed out (network to the vuln DB may be blocked).'}

    raw = proc.stdout.strip()
    if not raw:
        return {'ok': False, 'error': (proc.stderr or 'no output').strip()[:400]}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {'ok': False, 'error': raw[:400]}

    deps = data.get('dependencies', data if isinstance(data, list) else [])
    vulns = []
    for dep in deps:
        for v in dep.get('vulns', []) or []:
            vulns.append({
                'package': dep.get('name'),
                'version': dep.get('version'),
                'id': v.get('id'),
                'fix_versions': v.get('fix_versions', []),
                'description': (v.get('description') or '')[:200],
            })
    return {'ok': True, 'vulnerability_count': len(vulns), 'vulnerabilities': vulns[:100],
            'packages_checked': len(deps)}
