def chatbot_response(user_input):
    user_input = user_input.lower()


    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif 'your name' in user_input:
        return "I'm Chatbot, your virtual assistant."
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


def main():
    print("Chatbot: Hi! I'm Chatbot. How can I help you?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if 'bye' in user_input or 'goodbye' in user_input:
            break

if __name__ == "__main__":
    main()
