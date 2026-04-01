import os
from memory import Memory

def run():
    memory = Memory()

    print("🤖 AI Chatbot started! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        memory.add_user_message(user_input)

        # Demo mode
        if not os.getenv("OPENAI_API_KEY"):
            response = "This is a demo response. Add your API key to enable real AI."
        else:
            from agent import get_response
            response = get_response(memory)

        memory.add_ai_message(response)

        print(f"AI: {response}\n")

if __name__ == "__main__":
    run()
