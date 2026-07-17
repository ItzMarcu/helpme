from query import connect
from subprocess import run

def check_command(command: str = None):
    if not command: 
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

                choice = input("Want to run this command? (y/N): ").lower() or "n"
                if choice == "y":
                    run(response.split())
        
            except Exception as e: 
                print(f"Error: {e}")
        except KeyboardInterrupt: 
            return

if __name__ == "__main__":
    main()