
from datetime import datetime

print("Welcome to Python Chatbot!")
print("Ask me something. Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in message:
        print("Bot: I am a Python rule-based chatbot.")

    elif "python" in message:
        print("Bot: Python is a popular programming language.")

    elif "time" in message:
        print("Bot: Current time is",
              datetime.now().strftime("%I:%M %p"))

    elif "date" in message:
        print("Bot: Today's date is",
              datetime.now().strftime("%d-%m-%Y"))

    elif "thank" in message:
        print("Bot: You are welcome!")

    elif message in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
