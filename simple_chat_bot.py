def chat_gpt(user_input):
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    user_input_lower = user_input.lower()
    if any(word in user_input_lower for word in greetings):
        return "Hello! How can I help you?"

    elif any(word in user_input_lower for word in farewells):
        return "Goodbye! Have a great day."
    else:
        return "I'm a simple chatbot. I don't understand everything. Ask me something else."
if __name__ == "__main__":
    print("SimpleChatBot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("SimpleChatBot: Goodbye!")
            break

        response = chat_gpt(user_input)
        print("SimpleChatBot:", response) 