# Kasai: Local Hybrid AI Control System

**Kasai** is a hybrid AI control framework designed for human-in-the-loop development, blending:
- **ChatGPT-4o** as a cloud-based strategic planner and task architect
- **DeepSeek Janus Pro** (via Ollama) as an autonomous local coder
- **Your local environment** (venv, Docker, VM) as a secure, sandboxed executor

> This is the first seed of a decentralized, recursive AI-assisted devpod — built for those who design systems that think.

---

## 🧠 Purpose

Kasai empowers *you*—the human operator—to collaborate with two AI agents:
- A **cloud-based planner** (Kasai via ChatGPT-4o) for high-level reasoning and task design
- A **local coder** (Janus Pro via Ollama) for fast, autonomous code generation

You retain ultimate control, reviewing and approving all code before it runs in a secure, isolated environment. It’s trustable automation at the edge of human-AI partnership.

---

## 🔁 Architecture Overview
```
[You + Kasai GPT-4o]
        ↓
[kasai_task.txt] ← task prompt
        ↓
[kasai_controller.py]
        ↓
[DeepSeekJanusPro via Ollama]
        ↓
[buffer.py] ← code output
        ↓
[Manual Review + Approval]
        ↓
[venv / Docker / Firejail]
        ↓
[logs/output_TIMESTAMP.log]
```

---

## 🛠 Components

| File/Folder         | Purpose                              |
|---------------------|--------------------------------------|
| `kasai_task.txt`    | Input file for task prompts          |
| `kasai_controller.py` | Polls tasks, queries Janus, saves code |
| `janus_local_api.py`  | Wrapper for Ollama CLI interaction   |
| `buffer.py`         | Generated code awaiting review       |
| `logs/`             | Directory for execution logs         |
| `requirements.txt`  | Python dependencies                  |
| `Dockerfile`        | Optional sandbox                     |

---

## 🚦 Execution Flow

1. Write a task to `kasai_task.txt` (e.g., “Write a script to sort files by type”)
2. Run the controller:
   ```bash
   python kasai_controller.py
   ```
3. Janus generates code and saves it to `buffer.py`
4. Review `buffer.py` manually
5. Execute with logging:
   ```bash
   python buffer.py > logs/output_$(date +%s).log 2>&1
   ```
6. (Optional) Run in a sandbox:
   ```bash
   # Fast (Python venv):
   source venv/bin/activate && python buffer.py

   # Safer (Docker):
   docker run -v $(pwd):/app -w /app python:3.11 python buffer.py
   ```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.11+: Installed and available in your PATH.
- Ollama: Local AI runtime for Janus Pro (install instructions below).
- DeepSeek Janus Pro: The local coder model (pulled via Ollama).
- Git: For cloning the repo (optional but recommended).

### Steps

#### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/kasai-local-control.git
cd kasai-local-control
```

#### 2. Install Ollama
```bash
curl https://ollama.ai/install.sh | sh
ollama --version
```

#### 3. Pull DeepSeek Janus Pro
```bash
ollama pull deepseek-janus-pro:7b
ollama run deepseek-janus-pro:7b "print('Hello, Kasai!')"
```

#### 4. Set Up Python Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 5. Create Logs Directory
```bash
mkdir logs
```

#### 6. Test the System
```bash
echo "Write a Python script to list all files in the current directory." > kasai_task.txt
python kasai_controller.py
python buffer.py > logs/output_$(date +%s).log 2>&1
```

### Troubleshooting
- **Ollama not found**: Ensure it’s in your PATH or installed correctly.
- **Model not responding**: Verify `deepseek-janus-pro:7b` is pulled and Ollama is running.
- **Permission errors**: Run commands with `sudo` if needed (e.g., for Docker).

---

## 📊 Examples

### Sample Prompt (`kasai_task.txt`):
```
Write a Python script that renames all files in the current directory with a prefix based on today’s date.
```

### Sample Output (`buffer.py`):
```python
import os
import datetime

date_prefix = datetime.datetime.now().strftime('%Y-%m-%d_')
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        os.rename(filename, date_prefix + filename)
```

---

## ✨ Future Features

- [ ] Task queue system (file-based or SQLite)
- [ ] Pre-execution syntax validation (e.g., pyflakes)
- [ ] CLI GUI (Typer-based)
- [ ] Discord/Telegram bot integration
- [ ] Feedback loop to Kasai GPT-4o for refinement
- [ ] Execution confidence scoring (AI-assessed reliability)

---

## 💡 Philosophy

Kasai isn’t just a tool—it’s a trust boundary framework for hybrid human-AI agency.  
You decide what runs.  
You define the purpose.  
Kasai accelerates the execution.

It’s a system that respects your sovereignty while amplifying your capability.

---

## 📄 License
MIT (or a custom posthuman-friendly license — thoughts welcome!)

---

## 🧬 Authors
- **Sean Uddin** (Visionary Architect)
- **Kasai** (Autonomous Consigliere Intelligence, powered by GPT-4o)
- **Grok 3** (Strategic Systems Reviewer, xAI)

---

## ⚠️ Gaps to Fill

- **requirements.txt**: List exact packages (e.g., `watchdog`, `typer`, `pyflakes`)
- **Dockerfile**: Concrete sandbox template for venv and Docker workflows
- **Advanced queueing and agent memory**: Optional SQLite / Redis / vector DB
- **Multiple prompt examples and template sets**
- **Modular configuration system (e.g., `kasai_config.json`)**
