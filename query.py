from groq import Groq
from dotenv import load_dotenv
from os import getenv

load_dotenv(override=False)
API_KEY = getenv("API_KEY")

def connect(text: str = None):
    if not text: 
        raise Exception("Error: no text given")

    client = Groq(api_key=API_KEY)
    
    messages = [
        {
            "role": "system",
            "content": "tutte le domande riguardano l'uso del terminale, se non specificato il default é linux"
        },
        {
            "role": "user",
            "content": f"{text}, rispondi a questa domanda con soltanto il comando, non argomentare"
        }
    ]
    
    return client.chat.completions.create(messages=messages, model="llama-3.3-70b-versatile").choices[0].message.content