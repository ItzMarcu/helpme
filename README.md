# CommandsCLI

An ultra-lightweight, containerized Command Line Interface (CLI) assistant powered by Llama 3.3 (via Groq) that translates natural language queries into instant, precise terminal commands. 

---

## How It Works

CommandsCLI runs inside a highly optimized, rootless container (Podman or Docker) based on Alpine Linux. 
1. You pass your query in natural language (e.g., "how to update system packages").
2. The query is securely sent to the Groq API using your local API key.
3. The LLM processes the request and outputs only the raw terminal command.
4. The CLI executes the command directly inside your current host directory via container volume mounting.

---

## Requirements

- Podman or Docker installed on your system.
- A Groq API Key (Get one for free at https://console.groq.com/).

---

## Setup & Configuration

### 1. Configure your Environment Variables
Create a .env file in the root of the project directory and add your Groq API Key without quotes or spaces:

API_KEY=gsk_your_actual_groq_api_key_here

*Note: Avoid quotes around the key, as container runtimes pass them literally, which causes Authentication (401) errors.*

### 2. Build the Container Image

You can build the image using either Podman (recommended) or Docker.

#### Using Podman:
podman build -t commands-cli .

#### Using Docker:
docker build -t commands-cli .

---

## Creating a Global Alias (Shell Integration)

To allow CommandsCLI to execute commands directly inside the directory you are currently browsing in your terminal, the container must mount your current working directory (pwd).

### Linux & macOS

First, find the absolute path to your .env file by running "pwd" inside your project directory. 
Example path: /home/user/workspace/CommandsCLI/.env.

#### 1. For Zsh (Default on macOS & modern Linux distros)
Open your ~/.zshrc file:
nano ~/.zshrc

Add the following line at the end (replace /absolute/path/to/your/... with your actual path):
- Using Podman (Recommended):
  alias helpme="podman run --rm -it --userns=keep-id --env-file /absolute/path/to/your/CommandsCLI/.env -v \\"\\$(pwd)\\"/workspace:Z commands-cli"
- Using Docker:
  alias helpme="docker run --rm -it -v \\"\\$(pwd)\\"/workspace -w /workspace --env-file /absolute/path/to/your/CommandsCLI/.env commands-cli"

#### 2. For Bash
Open your ~/.bashrc file:
nano ~/.bashrc

Add the exact same alias line shown above.

#### Apply the changes:
source ~/.zshrc  # or source ~/.bashrc

---

### Windows

On Windows, you can map your current working directory using the ${PWD} variable.

#### 1. PowerShell (Recommended)
Open or create your PowerShell Profile:
notepad $PROFILE

Add the following function to dynamically mount your current host directory (replace with your absolute Windows path, e.g., C:\\Users\\User\\CommandsCLI\\.env):

- Using Podman:
  function Get-TerminalHelper {
      podman run --rm -it --env-file "C:\\path\\to\\your\\CommandsCLI\\.env" -v "${PWD}:/workspace" commands-cli
  }
  Set-Alias -Name helpme -Value Get-TerminalHelper

- Using Docker:
  function Get-TerminalHelper {
      docker run --rm -it --env-file "C:\\path\\to\\your\\CommandsCLI\\.env" -v "${PWD}:/workspace" -w /workspace commands-cli
  }
  Set-Alias -Name helpme -Value Get-TerminalHelper

Save and close the file, then reload your profile:
& $PROFILE

#### 2. Command Prompt (CMD)
Create a batch file named helpme.bat and place it in a directory that is in your Windows system PATH (e.g., C:\\Windows):

@echo off
podman run --rm -it --env-file "C:\\path\\to\\your\\CommandsCLI\\.env" -v "%cd%:/workspace" commands-cli

*(If using Docker, add -w /workspace and replace "podman" with "docker" in the command above).*

---

## Usage

Now, open a brand new terminal, navigate to any directory on your computer, and simply run:

helpme

### Example session:
marcuandre@desktop-andre:~$ helpme
q: elimina la cartella temp
rm -rf temp
Want to run this command? (y/N): y
q: exit

---

## Contributors

A special thanks to everyone who helped improve this project:

* [@gandzekas](https://github.com/gandzekas) - Implemented dangerous command detection.
