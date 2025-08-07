# Simple Predefined Reply Chatbot

# Dictionary of predefined responses
predefined_replies = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but thanks for asking!",
    "what is your name": "I'm a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "help": "Sure! I'm here to answer your basic questions."
}

# Default reply if input is not recognized
default_reply = "I'm sorry, I don't understand that. Can you try saying it differently?"

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()zz
        
        if user_input == "bye":
            print("Chatbot: Goodbye! 👋")
            break
        
        # Find a predefined response
        reply = predefined_replies.get(user_input, default_reply)
        print(f"Chatbot: {reply}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
