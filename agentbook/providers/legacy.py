"""Compatibility helper for chapters that have not adopted ``Backend`` yet."""

from __future__ import annotations

from .resolution import resolve_backend

__all__ = ["resolve_llm_backend"]


def resolve_llm_backend(primary_key: str | None, primary_base_url: str, model: str) -> tuple[str, str, str, bool]:
    """Resolve an OpenAI tuple while preserving the legacy function shape."""
    del primary_base_url
    return tuple(resolve_backend("openai", model=model, api_key=primary_key))
