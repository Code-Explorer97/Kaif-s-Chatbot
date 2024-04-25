import random

# Define a dictionary with basic responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I help you?"],
    "how are you": ["I'm a bot, I'm always good!", "Doing well, thanks!", "I'm fine, thank you for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
}

def chatbot():
    print("Welcome to the chatbot! Type something to begin (type 'bye' to exit).")
    
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot: " + random.choice(responses[user_input]))
        else:
            print("Bot: I'm not sure how to respond to that.")
        
        if user_input == "bye":
            break

# Run the chatbot
chatbot()