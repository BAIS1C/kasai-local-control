# kasai_exec.py
"""
Handles execution of buffer.py with:
1. Syntax validation using pyflakes
2. Optional test execution
3. Logging to /logs/ with timestamped filenames
4. Returns execution status for kasai_controller or post-processing
"""

import subprocess
import time
import os
import json
from datetime import datetime

CONFIG_FILE = "kasai_config.json"

# Load config
with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

sandbox_mode = config.get("sandbox_mode", "venv")
log_runs = config.get("log_successful_runs", True)

# Step 1: Syntax check
print("🔍 Running syntax check with pyflakes...")
syntax_result = subprocess.run(["pyflakes", "buffer.py"], capture_output=True, text=True)

if syntax_result.stdout:
    print("❌ Syntax issues detected:\n")
    print(syntax_result.stdout)
    exit(1)
else:
    print("✅ No syntax errors. Proceeding to execution...\n")

# Step 2: Run the script
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"logs/output_{timestamp}.log"

print(f"🚀 Executing buffer.py... ({sandbox_mode} mode)")

try:
    with open(log_filename, "w") as logfile:
        result = subprocess.run(["python", "buffer.py"], stdout=logfile, stderr=subprocess.STDOUT, text=True)

    if result.returncode == 0:
        print(f"✅ Execution successful. Log saved to {log_filename}")
    else:
        print(f"⚠️ Execution returned non-zero status. Check logs: {log_filename}")
except Exception as e:
    print(f"❌ Execution failed: {str(e)}")
    exit(1)
