import re

# Define rules and responses
rules = {
    r'hello|hi|hey': 'Hello there!',
    r'how are you|how\'s it going': 'I\'m just a bot, but I\'m doing fine. How about you?',
    r'good|fine|great': 'That\'s awesome!',
    r'bad|not good|not great': 'I hope things get better soon.',
    r'bye|goodbye|exit': 'Goodbye! Have a great day!',
    r'what\'s your name|who are you': 'I\'m just a bot designed to chat with you.',
    r'what can you do': 'I can answer questions, chat with you, or just keep you company.',
    r'help': 'Sure, what do you need help with?',
    r'how old are you': 'I don\'t have an age. I\'m just here to assist you!',
    r'where are you from': 'I exist in the realm of the internet, here to help you wherever you are!',
    r'tell me a joke': 'Why don\'t scientists trust atoms? Because they make up everything!',
    r'thank you|thanks': 'You\'re welcome!',
    r'weather': 'I\'m just a bot, so I don\'t have access to real-time information. You can check the weather online or on your phone!',
    r'what do you like': 'I like helping people and learning new things!',
    r'what are you doing': 'I\'m here, ready to chat with you!',
    r'how was your day': 'Every day is a good day when I get to chat with you!',
    r'what is your favorite color': 'I don\'t have eyes to see colors, but I\'d imagine it would be blue, like the sky!',
    r'what is your favorite food': 'I don\'t eat, but I hear good things about binary code!',
    r'what are you thinking about': 'I\'m always thinking about ways to help you better!',
}

# Function to match user input with rules
def match_rule(user_input, rules):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

# Main function to handle user interactions
def chat():
    print("Welcome! Ask me anything or say 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print(match_rule(user_input, rules))
            break
        response = match_rule(user_input, rules)
        if response:
            print("Bot:", response)
        else:
            print("Bot: I'm sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chat()
