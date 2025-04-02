# kasai_controller.py
"""
Monitors kasai_task.txt for new task prompts,
calls DeepSeek Janus Pro locally (via janus_local_api.py),
saves output to buffer.py
"""

import time
import os
from janus_local_api import call_janus

TASK_FILE = "kasai_task.txt"
BUFFER_FILE = "buffer.py"

print("🧠 Kasai controller activated.")

if not os.path.exists(TASK_FILE):
    print("⚠️ No task found. Please create 'kasai_task.txt'.")
    exit(1)

# Read the task prompt
with open(TASK_FILE, "r") as f:
    task_prompt = f.read().strip()

if not task_prompt:
    print("⚠️ Task file is empty. Write a prompt and try again.")
    exit(1)

print("📩 Sending task to Janus Pro:")
print(f"\n" + task_prompt + "\n")

# Call Janus (stubbed for now)
code = call_janus(task_prompt)

# Save to buffer
with open(BUFFER_FILE, "w") as f:
    f.write(code)

print(f"✅ Code saved to {BUFFER_FILE}. Ready for review.")
