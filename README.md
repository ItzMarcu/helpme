# CommandsCLI

An ultra-lightweight, containerized Command Line Interface (CLI) assistant powered by Llama 3.3 (via Groq) that translates natural language queries into instant, precise terminal commands. 

---

## How It Works

CommandsCLI runs inside a highly optimized, rootless container (Podman or Docker) based on Alpine Linux. 
1. You pass your query in natural language (e.g., "how to update system packages").
2. The query is securely sent to the Groq API using your local API key.
3. The LLM processes the request and outputs only the raw terminal command, ready to be copied.

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

To make commands-cli run instantly from any directory using a simple keyword like helpme, set up a global alias for your operating system and terminal shell.

### Linux & macOS

First, find the absolute path to your .env file by running "pwd" inside your project directory. 
Example path: /home/user/workspace/CommandsCLI/.env or /Users/user/workspace/CommandsCLI/.env.

#### 1. For Zsh (Default on macOS & Linux Mint/Ubuntu/Debian modern shells)
Open your ~/.zshrc file:
nano ~/.zshrc

Add the following line at the end (replace with your absolute path):
- Using Podman:
  alias helpme="podman run --rm -it --env-file /absolute/path/to/your/CommandsCLI/.env commands-cli"
- Using Docker:
  alias helpme="docker run --rm -it --env-file /absolute/path/to/your/CommandsCLI/.env commands-cli"

#### 2. For Bash (Default on older Linux distros and Git Bash on Windows)
Open your ~/.bashrc file:
nano ~/.bashrc

Add the same alias line as shown above.

#### Apply the changes:
source ~/.zshrc  # or source ~/.bashrc

---

### Windows

On Windows, you can configure an alias depending on whether you use PowerShell or the classic Command Prompt (CMD).

#### 1. PowerShell (Recommended)
Open or create your PowerShell Profile:
notepad $PROFILE

Add the following function to map helpme dynamically (replace with your absolute Windows path, e.g., C:\Users\User\CommandsCLI\.env):

- Using Podman:
  function Get-TerminalHelper {
      podman run --rm -it --env-file "C:\path\to\your\CommandsCLI\.env" commands-cli
  }
  Set-Alias -Name helpme -Value Get-TerminalHelper

- Using Docker:
  function Get-TerminalHelper {
      docker run --rm -it --env-file "C:\path\to\your\CommandsCLI\.env" commands-cli
  }
  Set-Alias -Name helpme -Value Get-TerminalHelper

Save and close the file, then reload your profile:
& $PROFILE

#### 2. Command Prompt (CMD)
Create a batch file named helpme.bat and place it in a directory that is in your Windows system PATH (e.g., C:\Windows or a custom tools folder):

@echo off
podman run --rm -it --env-file "C:\path\to\your\CommandsCLI\.env" commands-cli

*(If using Docker, replace "podman" with "docker" in the command above).*

---

## Usage

Now, open a brand new terminal, navigate to any directory, and simply run:

helpme

### Example session:
q: how to unzip a file to a specific folder
unzip archive.zip -d /path/to/destination

q: list all open ports on my system
ss -tuln

q: exit

---
