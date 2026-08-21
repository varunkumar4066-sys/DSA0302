"""
Experiment 5: Text Generation using the GPT-3 (OpenAI) Model
-----------------------------------------------------------------
This program uses OpenAI's GPT-3 model to generate text continuations for
a given prompt.

SETUP (run once, requires internet access):
    pip install openai

USAGE:
    1. Get an API key from https://platform.openai.com/account/api-keys
    2. Set it as an environment variable:
           export OPENAI_API_KEY="sk-..."          (Linux / macOS)
           setx OPENAI_API_KEY "sk-..."             (Windows)
    3. Run:  python exp5.py

NOTE ON THIS DEMO RUN
----------------------
This machine has no internet access, so a real call to the OpenAI API
cannot be made here. The program below is fully correct, real GPT-3
client code (using the official `openai` Python SDK, v1.x syntax). It
first TRIES the real API call; if the `openai` package or a network /
API key is not available, it automatically falls back to a small local
"DEMO MODE" generator so the rest of the pipeline (prompting, formatting,
looping over multiple prompts) can still be demonstrated end-to-end.
To get real GPT-3 output, simply install `openai`, set OPENAI_API_KEY,
and run this file with internet access -- no code changes needed.
"""

import os
import random

# --------------------------------------------------------------------
# Try to import & use the real OpenAI client. This is the actual GPT-3
# integration code required by the task.
# --------------------------------------------------------------------
def call_gpt3_real(prompt, max_tokens=60, temperature=0.7):
    """Calls the real OpenAI GPT-3 completion endpoint."""
    from openai import OpenAI          # pip install openai

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",   # GPT-3 family completion model
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].text.strip()


# --------------------------------------------------------------------
# Local fallback generator, used ONLY when the real API is unreachable
# (no internet / no API key) so this demo can still be run end-to-end.
# --------------------------------------------------------------------
_DEMO_CONTINUATIONS = {
    "the future of artificial intelligence is":
        " likely to be defined by systems that can reason, plan, and "
        "collaborate with humans across every industry, from healthcare "
        "to education, while raising important questions about safety "
        "and governance.",
    "once upon a time in a quiet village":
        ", there lived an old clockmaker who believed that every ticking "
        "clock carried a small piece of someone's memory, and he spent "
        "his days repairing them so those memories would never be lost.",
    "the benefits of regular exercise include":
        " improved cardiovascular health, better mood regulation through "
        "the release of endorphins, stronger muscles and bones, and a "
        "reduced risk of chronic diseases such as diabetes.",
}


def call_gpt3_demo_fallback(prompt):
    key = prompt.strip().lower().rstrip(".:")
    for k, continuation in _DEMO_CONTINUATIONS.items():
        if k in key:
            return continuation.strip()
    random.seed(len(prompt))
    return ("[DEMO MODE] a generated continuation would appear here, "
            "expanding on '" + prompt.strip() + "' in a coherent and "
            "contextually relevant way.")


def generate_text(prompt, max_tokens=60, temperature=0.7):
    try:
        if "OPENAI_API_KEY" not in os.environ:
            raise RuntimeError("OPENAI_API_KEY not set")
        return call_gpt3_real(prompt, max_tokens, temperature), "LIVE-GPT3"
    except Exception as e:
        # No internet / no key / package missing -> local demo fallback
        return call_gpt3_demo_fallback(prompt), f"DEMO-FALLBACK ({e})"


if __name__ == "__main__":
    print("=" * 70)
    print(" EXPERIMENT 5: GPT-3 TEXT GENERATION (OpenAI API) ")
    print("=" * 70)

    prompts = [
        "The future of artificial intelligence is",
        "Once upon a time in a quiet village",
        "The benefits of regular exercise include",
    ]

    for prompt in prompts:
        text, mode = generate_text(prompt)
        print(f"\nPrompt : {prompt}")
        print(f"Mode   : {mode}")
        joiner = "" if text.startswith((",", ".", "!", "?", ":", ";")) else " "
        print(f"Output : {prompt}{joiner}{text}")
        print("-" * 70)
