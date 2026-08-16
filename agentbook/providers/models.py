"""Dataclasses describing the OpenAI backend."""

from __future__ import annotations

import os
from dataclasses import dataclass

__all__ = ["Backend", "Provider"]


@dataclass(frozen=True)
class Provider:
    """Static description of the supported backend."""

    name: str
    base_url: str
    default_model: str
    key_vars: tuple[str, ...] = ()

    def api_key(self) -> str:
        """Read the first configured API key from the environment."""
        for var in self.key_vars:
            value = os.getenv(var, "").strip()
            if value:
                return value
        return ""


@dataclass(frozen=True)
class Backend:
    """A resolved, ready-to-use OpenAI endpoint."""

    api_key: str
    base_url: str
    model: str
    provider: str

    @property
    def using_openrouter(self) -> bool:
        """Retain the legacy status field; the OpenAI-only resolver never reroutes."""
        return False

    def __iter__(self):
        """Unpack as the legacy four-item backend tuple."""
        return iter((self.api_key, self.base_url, self.model, False))
