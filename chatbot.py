
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "👋 Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "😊 I'm just a bot, but I'm doing great! Thanks for asking."
    elif "name" in user_input:
        return "🤖 I'm a simple chatbot created with Python."
    elif "bye" in user_input:
        return "👋 Goodbye! Have a great day!"
    else:
        return "🤔 Sorry, I don't understand that."


def main():
    print("🤖 Chatbot is running! Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
