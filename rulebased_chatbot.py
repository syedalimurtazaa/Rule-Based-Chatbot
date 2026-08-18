
import random


# STEP 1: Define keyword groups.
# Each topic has a list of trigger words/phrases we look for in user input.

KEYWORDS = {
    "greeting": ["hello", "hi", "hey", "salaam", "assalam", "yo"],
    "farewell": ["bye", "goodbye", "see you", "exit", "quit"],
    "how_are_you": ["how are you", "how're you", "how you doing"],
    "bot_name": ["your name", "who are you", "what are you called"],
    "user_name": ["my name is", "i am ", "i'm "],
    "help": ["help", "what can you do", "commands"],
    "thanks": ["thank", "thanks", "shukriya"],
    "age": ["how old are you", "your age"],
    "creator": ["who made you", "who created you", "who built you"],
    "mood_good": ["i am fine", "i'm fine", "i am good", "i'm good", "doing well"],
    "mood_bad": ["i am sad", "i'm sad", "not good", "feeling bad", "i am tired"],
    "joke": ["joke", "make me laugh", "funny"],
}

# STEP 2: Define possible responses for each topic.
# Using LISTS (not single strings) lets us randomly pick one each time,
# so the bot doesn't sound identical every time (bonus: response variety).

RESPONSES = {
    "greeting": [
        "Hello there! How can I help you today?",
        "Hi! Nice to hear from you.",
        "Hey! What's up?",
    ],
    "farewell": [
        "Goodbye! Have a great day.",
        "See you later!",
        "Bye! Take care.",
    ],
    "how_are_you": [
        "I'm just a program, but I'm running smoothly! How about you?",
        "Doing great, thanks for asking! How are you?",
    ],
    "bot_name": [
        "I'm ChatBuddy, your friendly rule-based chatbot.",
        "You can call me ChatBuddy!",
    ],
    "user_name": [
        "Nice to meet you!",
        "Got it, I'll remember that (well, for this session at least).",
    ],
    "help": [
        "I can chat about greetings, farewells, your mood, my name, "
        "and even tell a joke. Try saying 'hi', 'joke', or 'bye'.",
        "Try asking things like 'how are you', 'what's your name', "
        "or just say 'bye' to leave.",
    ],
    "thanks": [
        "You're welcome!",
        "No problem at all!",
        "Anytime!",
    ],
    "age": [
        "I don't have an age, I'm just lines of code!",
        "Ageless, that's one perk of being a chatbot.",
    ],
    "creator": [
        "I was built by a developer practicing Python chatbot basics.",
        "A curious Python programmer created me!",
    ],
    "mood_good": [
        "That's awesome to hear!",
        "Glad you're doing well!",
    ],
    "mood_bad": [
        "I'm sorry to hear that. I hope things get better soon.",
        "That's tough, take care of yourself.",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to the doctor? It had a virus!",
    ],
}

# Fallback replies when no keyword matches (also randomized).

FALLBACK_RESPONSES = [
    "Sorry, I didn't understand that. Could you rephrase?",
    "Hmm, I'm not sure what you mean. Try asking something else.",
    "I don't have an answer for that yet. Type 'help' to see what I can do.",
]

# Words that end the conversation.

EXIT_WORDS = {"bye", "goodbye", "exit", "quit"}


def get_response(user_input: str) -> str:
    """
    Takes the raw user input, checks it against our keyword dictionary,
    and returns a matching response (or a fallback if nothing matches).
    """
    text = user_input.lower().strip()  

# Loop through each topic and its keyword list.

    for topic, keyword_list in KEYWORDS.items():
        for keyword in keyword_list:
            if keyword in text:  
                return random.choice(RESPONSES[topic])

# No keyword matched -> fallback

    return random.choice(FALLBACK_RESPONSES)


def is_exit(user_input: str) -> bool:
    """Check if the user typed a word that means they want to leave."""
    text = user_input.lower().strip()
    return any(word in text for word in EXIT_WORDS)


def main():
    """
    Main chat loop:
    - Keeps asking for input until the user says bye/exit/quit.
    - Counts how many messages were exchanged (bonus feature).
    """
    print("=" * 50)
    print(" ChatBuddy - Rule Based Chatbot")
    print(" Type 'help' to see what I can do, or 'bye' to exit.")
    print("=" * 50)

# tracks number of user messages sent this session
    message_count = 0  

    while True:
        user_input = input("You: ")

# Ignore completely empty input (just pressing Enter).
        if user_input.strip() == "":
            print("Bot: Please type something!")
            continue

# count every real message
        message_count += 1  

        if is_exit(user_input):
            print(f"Bot: {random.choice(RESPONSES['farewell'])}")
            print(f"\n(Session summary: you sent {message_count} message(s). Goodbye!)")
            break  

        reply = get_response(user_input)
        print(f"Bot: {reply}")


# This ensures main() only runs when the script is executed directly,
# not when it's imported into another file.

if __name__ == "__main__":
    main()