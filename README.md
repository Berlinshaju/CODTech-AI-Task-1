# AI TASK ONE: CHATBOT WITH RULE-BASED RESPONSES
# Introduction:
The chatbot with rule-based responses project creates a simple conversational agent using Python. The chatbot interacts with users by responding to their messages based on predefined rules and patterns. This project provides an introduction to natural language processing and conversation flow in chatbot development.

# Code Explanation:
# Rules and Responses:
The chatbot's behavior is determined by a set of predefined rules and responses. Each rule is a regular expression pattern that matches specific user inputs, and the corresponding response is provided by the chatbot.

import re

# Define rules and responses
rules = {
    r'hello|hi|hey': 'Hello there!',
    r'how are you|how\'s it going': 'I\'m just a bot, but I\'m doing fine. How about you?',
    # Add more rules as needed
}


