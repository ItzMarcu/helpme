from query import connect
from subprocess import run
from pathlib import Path


def load_dangerous_patterns() -> list[str]:
    """Load dangerous command patterns from dangerous_commands.txt"""
    patterns = []
    danger_file = Path(__file__).parent / "assets/dangerous_commands.txt"
    if danger_file.exists():
        for line in danger_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line.lower())
    return patterns


DANGEROUS_PATTERNS = load_dangerous_patterns()


def check_command(command: str | None = None) -> bool:
    """
    Check if a command matches any dangerous pattern.
    Returns True if the command is dangerous, False otherwise.
    """
    if not command:
        return False
    cmd_lower = command.lower().strip()
    for pattern in DANGEROUS_PATTERNS:
        if pattern in cmd_lower:
            return True
    return False


def main():
    while True:
        try:
            user_question = input("q: ").strip()

            if user_question.lower() == "exit":
                return

            try:
                response = connect(user_question)
                if response:
                    print(response)

                # Check for dangerous commands before asking
                if check_command(response):
                    print("⚠️  WARNING: This command matches a dangerous pattern!")
                    print("   Executing it may cause data loss or system damage.")
                    choice = input("   Are you ABSOLUTELY sure? (yes/NO): ").strip().lower()
                    if choice != "yes":
                        print("   Command cancelled.")
                        continue
                else:
                    choice = input("Want to run this command? (y/N): ").lower() or "n"

                if choice == "y" or choice == "yes":
                    run(response.split())

            except Exception as e:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()