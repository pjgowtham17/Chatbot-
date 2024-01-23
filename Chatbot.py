# Chatbot-
import random

def simple_chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but I'm doing well. Thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure how to respond to that. Can you ask me something else?"
    }

    print("Simple Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("User: ").lower()

        if user_input == 'bye':
            print("Simple Chatbot: Goodbye!")
            break
        else:
            response = responses.get(user_input, responses["default"])
            print(f"Simple Chatbot: {response}")

if __name__ == "__main__":
    simple_chatbot()
