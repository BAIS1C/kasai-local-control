# janus_local_api.py
"""
Wrapper for calling DeepSeek Janus Pro 7B via Ollama locally.
"""

import subprocess

def call_janus(prompt):
    print("🛰️ Calling DeepSeek Janus Pro via Ollama...")
    try:
        result = subprocess.run(
            ["ollama", "run", "deepseek-janus-pro:7b", prompt],
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8',
            errors='replace'  # prevents crashes on weird chars
        )
        if result.returncode != 0:
            print("❌ Janus/Ollama error:", result.stderr)
            return "# ERROR: Janus failed"

        return result.stdout.strip()

    except Exception as e:
        print("❌ Exception calling Janus:", str(e))
        return "# ERROR: Exception occurred during Janus call"
