# kasai_git_committer.py
"""
Handles Git commit and push logic.
Only triggers when config['auto_commit'] == true AND kasai_exec succeeds.
Otherwise logs a message about readiness to commit manually.
"""

import subprocess
import json
from datetime import datetime

CONFIG_FILE = "kasai_config.json"
TASK_FILE = "kasai_task.txt"

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

AUTO_COMMIT = config.get("auto_commit", False)
DEFAULT_MESSAGE = config.get("default_git_message", "Kasai manual commit post-review")

# Optional: get task-based commit message
try:
    with open(TASK_FILE, "r") as f:
        task_prompt = f.read().strip()
        short_prompt = task_prompt.split("\n")[0][:64]
        commit_message = f"Kasai: {short_prompt}"
except Exception:
    commit_message = DEFAULT_MESSAGE

if not AUTO_COMMIT:
    print("📝 Auto-commit is disabled. Commit manually when ready.")
    print(f"🔖 Suggested commit message: \"{commit_message}\"")
else:
    try:
        subprocess.run(["git", "add", "buffer.py"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Kasai committed and pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("❌ Git error:", e)
