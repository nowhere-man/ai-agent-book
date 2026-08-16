"""Single source of truth for the OpenAI backend."""

from __future__ import annotations

from .legacy import resolve_llm_backend
from .models import Backend, Provider
from .registry import PROVIDERS, SUPPORTED_PROVIDERS, canonical_provider
from .resolution import resolve_backend

__all__ = [
    "PROVIDERS",
    "SUPPORTED_PROVIDERS",
    "Backend",
    "Provider",
    "canonical_provider",
    "resolve_backend",
    "resolve_llm_backend",
]
