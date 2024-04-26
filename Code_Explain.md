# CLI implementation of the chatbot:

# 1. Rules and Responses:
The **rules** dictionary is defined to store the patterns and their corresponding responses. Each key-value pair represents a rule, where the key is a regular expression pattern and the value is the response the chatbot should provide when the user's input matches that pattern.
Regular expressions are used to define flexible patterns that can match multiple variations of user input.

# 2. Match Rule Function:
The **match_rule** function is defined to match user input against the predefined rules.
It takes two parameters: **user_input** (the input provided by the user) and **rules** (the dictionary containing the predefined rules and responses).
The function iterates through each key-value pair in the rules dictionary.
For each pair, it uses the **re.search()** function to search for the pattern in the user's input.
If a match is found, it returns the corresponding response. If no match is found, it moves on to the next rule.
The **re.IGNORECASE** flag is used to make the pattern matching case-insensitive, allowing the chatbot to recognize patterns regardless of the case of the input.

# 3. Main Chat Function:
The **chat** function is defined to handle the main logic of the chatbot.
It starts by printing a welcome message, prompting the user to ask a question or say 'bye' to exit.
Inside a continuous **while** loop, it continuously accepts user input using the **input()** function.
If the user input matches any of the exit phrases ('bye', 'goodbye', 'exit'), the chatbot prints a farewell message and exits the loop.
Otherwise, it calls the **match_rule** function to find a response based on the user's input.
If a response is found, the chatbot prints it along with the prefix "Bot:". If no response is found, it prints a default message indicating that it didn't understand the input.
The loop continues until the user decides to exit.

# 4. Program Execution:
The if __name__ == "__main__": block ensures that the **chat** function is called only when the script is executed as the main program.
When the script is executed, the **chat** function is called, initiating the chatbot session.

# Conclusion:
The provided code implements a simple chatbot with rule-based responses using Python.
It defines rules and corresponding responses to enable the chatbot to engage in conversations with users.
The chatbot's behavior is driven by predefined patterns, allowing it to respond to various user inputs effectively. However, it may struggle with handling complex queries or understanding ambiguous input due to its rule-based approach.



# GUI implementation of the chatbot:

# 1. Importing Required Libraries:

The **re module** is imported to work with regular expressions.
The **tkinter module** is imported as **tk** to create the graphical user interface (GUI).
# 2. Define Rules and Responses:
The **rules** dictionary contains regular expression patterns as keys and corresponding responses as values. These rules define how the chatbot should respond to different user inputs.

# 3. Match Rule Function:
The **match_rule** function is defined to match user input against the predefined rules.
It takes two parameters: **user_input** (the input provided by the user) and **rules** (the dictionary containing the predefined rules and responses).
The function iterates through each key-value pair in the **rules** dictionary.
For each pair, it uses the **re.search()** function to search for the pattern in the user's input.
If a match is found, it returns the corresponding response. If no match is found, it moves on to the next rule.
The **re.IGNORECASE** flag is used to make the pattern matching case-insensitive, allowing the chatbot to recognize patterns regardless of the case of the input.

# 4. Send Message Function:
The **send_message** function is defined to handle user input and update the chat history displayed in the GUI.
It takes an optional **event** parameter, which allows the function to be triggered by pressing the Enter key in the entry field.
It retrieves the user input from the entry field using the **get()** method.
If the user input matches any of the exit phrases ('bye', 'goodbye', 'exit'), the chat history is updated with the user's input and a farewell message from the chatbot is displayed.
If the user input does not match an exit phrase, the chat history is updated with the user's input, and the chatbot's response (based on the predefined rules) is displayed.
The entry field is cleared after processing the user input.

# 5. Create the GUI:
The GUI window is created using **tk.Tk()** and titled "Chatbot".
Frames are used to organize different elements of the GUI.
A text widget **(chat_history)** is created to display the chat history, with a scrollbar **(scrollbar)** for scrolling through long conversations.
An entry field **(entry)** is created for users to input messages.
The entry field is bound to the send_message function, allowing users to press Enter to send messages.
A button **(send_button)** is created to trigger the **send_message** function when clicked.

# 6. Run the GUI:
The **mainloop()** method is called on the root window to start the GUI event loop, allowing the user to interact with the chatbot.

# Conclusion:
The provided code implements a chatbot with rule-based responses in a graphical user interface using Tkinter.
Users can input messages via an entry field and receive responses displayed in a chat history window.
The chatbot's behavior is determined by predefined rules, allowing it to respond to various user inputs effectivel




