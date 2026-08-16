"""Unit tests for the OpenAI-only provider configuration."""

import pytest

from config import resolve_llm_backend


def test_explicit_key_uses_openai_endpoint():
    assert resolve_llm_backend(
        "openai-key", "https://ignored.test/v1", "gpt-4o-mini"
    ) == (
        "openai-key",
        "https://api.openai.com/v1",
        "gpt-4o-mini",
        False,
    )


def test_environment_key_is_used_when_no_key_is_passed(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "environment-key")

    assert resolve_llm_backend(None, "https://ignored.test/v1", "gpt-4o") == (
        "environment-key",
        "https://api.openai.com/v1",
        "gpt-4o",
        False,
    )


def test_provider_resolution_requires_openai_key():
    with pytest.raises(ValueError, match="Set OPENAI_API_KEY"):
        resolve_llm_backend(None, "https://ignored.test/v1", "gpt-4o")
