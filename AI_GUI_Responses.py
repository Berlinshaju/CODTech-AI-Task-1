import re
import tkinter as tk

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

# Function to handle user input and update chat history
def send_message(event=None):
    user_input = entry.get()
    if user_input.lower() in ['bye', 'goodbye', 'exit']:
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        chat_history.insert(tk.END, match_rule(user_input, rules) + "\n")
        entry.delete(0, tk.END)
    else:
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        response = match_rule(user_input, rules)
        if response:
            chat_history.insert(tk.END, "Bot: " + response + "\n")
        else:
            chat_history.insert(tk.END, "Bot: I'm sorry, I didn't understand that.\n")
        entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Chatbot")

# Create a frame to hold the chat history
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Create a scrollbar for the chat history
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget to display the chat history
chat_history = tk.Text(chat_frame, width=50, height=20, yscrollcommand=scrollbar.set)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_history.yview)

# Create a frame to hold the input field and send button
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create an entry field for user input
entry = tk.Entry(input_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 5))

# Bind the entry field to the send_message function
entry.bind("<Return>", send_message)

# Create a button to send the message
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Run the GUI
root.mainloop()
