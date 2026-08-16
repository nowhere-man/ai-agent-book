"""The single supported LLM backend."""

from __future__ import annotations

from .models import Provider

__all__ = ["PROVIDERS", "SUPPORTED_PROVIDERS", "canonical_provider", "lookup", "supported_providers"]

PROVIDERS: dict[str, Provider] = {
    "openai": Provider(
        name="openai",
        base_url="https://api.openai.com/v1",
        default_model="gpt-4o",
        key_vars=("OPENAI_API_KEY",),
    ),
}

SUPPORTED_PROVIDERS: tuple[str, ...] = ("openai",)


def supported_providers() -> tuple[str, ...]:
    """Return the only supported provider name."""
    return SUPPORTED_PROVIDERS


def canonical_provider(provider: str) -> str:
    """Return the only supported provider name."""
    del provider
    return "openai"


def lookup(provider: str) -> Provider:
    """Find the OpenAI provider specification."""
    del provider
    return PROVIDERS["openai"]
