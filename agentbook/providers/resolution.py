"""Resolution policy for the OpenAI backend."""

from __future__ import annotations

from .models import Backend
from .registry import lookup

__all__ = ["resolve_backend"]


def resolve_backend(provider: str, model: str | None = None, api_key: str | None = None) -> Backend:
    """Resolve the OpenAI backend from an explicit or environment key."""
    spec = lookup(provider)
    key = (api_key or "").strip() or spec.api_key()
    if not key:
        raise ValueError("No API key found. Set OPENAI_API_KEY.")
    return Backend(key, spec.base_url, (model or "").strip() or spec.default_model, spec.name)
