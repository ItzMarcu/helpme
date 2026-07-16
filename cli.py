from query import connect

def main():
    while True:
        user_question = input("q: ").strip()
        
        if user_question.lower() == "exit":
            return
        
        try: 
            response = connect(user_question)
            if response: 
                print(response)
            
        
        except Exception as e: 
            print(f"Error: {e}")

if __name__ == "__main__":
    main()