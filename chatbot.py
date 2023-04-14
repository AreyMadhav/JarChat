# Import necessary libraries
import random

# Define possible user inputs and corresponding chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thank you for asking!", "I'm feeling great today!"],
    "what is your name": ["My name is ChatBot!", "I'm ChatBot!", "I'm called ChatBot!"],
    "bye": ["Goodbye!", "Bye!", "See you later!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."]
}

# Define function to get chatbot response
def get_response(user_input):
    # Convert input to lowercase and remove whitespace
    user_input = user_input.lower().strip()
    
    # Check if input is in responses dictionary
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Define main function to run chatbot
def main():
    print("Hi, I'm ChatBot! What can I help you with today?")
    while True:
        user_input = input("User: ")
        if user_input == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("ChatBot:", response)

# Run main function
if __name__ == "__main__":
    main()
