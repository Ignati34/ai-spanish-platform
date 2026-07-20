"""Rough AI cost estimation for usage metering.

Rates are USD estimates for OpenAI-compatible models; they exist so the admin
Usage & Costs view has meaningful numbers. They are intentionally easy to adjust
and are NOT billing-grade. Chat rates are per 1K tokens; audio is per second;
images are per image.
"""
from __future__ import annotations

# (input_per_1k, output_per_1k) in USD
_CHAT_PRICING: dict[str, tuple[float, float]] = {
    'gpt-4o-mini': (0.00015, 0.00060),
    'gpt-4o': (0.00250, 0.01000),
    'gpt-4.1-mini': (0.00040, 0.00160),
    'gpt-4.1': (0.00200, 0.00800),
    'gpt-4.1-nano': (0.00010, 0.00040),
    'o4-mini': (0.00110, 0.00440),
}
_DEFAULT_CHAT = (0.00050, 0.00150)

# Audio, USD per second (STT ~ $0.006/min; TTS is really per-char, approximated here).
_STT_PER_SEC = 0.0001
_TTS_PER_SEC = 0.00025
_IMAGE_EACH = 0.01


def _chat_rates(model: str | None) -> tuple[float, float]:
    if not model:
        return _DEFAULT_CHAT
    key = model.lower()
    if key in _CHAT_PRICING:
        return _CHAT_PRICING[key]
    # prefix match (e.g. dated snapshots like gpt-4o-mini-2024-xx)
    for name, rates in _CHAT_PRICING.items():
        if key.startswith(name):
            return rates
    return _DEFAULT_CHAT


def estimate_chat_cost(model: str | None, input_tokens: int, output_tokens: int) -> float:
    rin, rout = _chat_rates(model)
    return round((input_tokens / 1000.0) * rin + (output_tokens / 1000.0) * rout, 6)


def estimate_audio_cost(seconds: float, kind: str = 'stt') -> float:
    rate = _TTS_PER_SEC if kind == 'tts' else _STT_PER_SEC
    return round(max(0.0, float(seconds)) * rate, 6)


def estimate_image_cost(count: int) -> float:
    return round(max(0, int(count)) * _IMAGE_EACH, 6)
