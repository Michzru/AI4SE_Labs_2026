"""Shared OpenAI chat helper (API key from code/.env, variable API_KEY)."""
from __future__ import annotations

import os
import time
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

HERE = Path(__file__).resolve().parent

# models from the course constraint list that this API project can reach
# (gpt-4.1-nano returns 404 – deprecated)
MODELS = ["gpt-6-luna", "gpt-5.6-luna", "gpt-5.4-nano", "gpt-5-nano", "gpt-5-mini", "gpt-4o-mini"]
NO_REASONING = {"gpt-4o-mini"}  # rejects the reasoning_effort argument


@lru_cache(maxsize=1)
def client() -> OpenAI:
    load_dotenv(HERE / ".env")
    return OpenAI(api_key=os.environ["API_KEY"], max_retries=5)


def chat(model: str, system: str, user: str) -> dict:
    """Single chat completion; returns text, token usage and latency."""
    kwargs = {} if model in NO_REASONING else {"reasoning_effort": "low"}
    t0 = time.perf_counter()
    resp = client().chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        **kwargs,
    )
    return {
        "text": (resp.choices[0].message.content or "").strip(),
        "prompt_tokens": resp.usage.prompt_tokens,
        "completion_tokens": resp.usage.completion_tokens,
        "seconds": round(time.perf_counter() - t0, 2),
    }
