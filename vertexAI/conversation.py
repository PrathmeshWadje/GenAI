import vertexai
from vertexai.generative_models import GenerativeModel


def create_session():
    vertexai.init(project="finalyearproject-adypu", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-001")
    chat = model.start_chat()
    return chat

def response(chat, message):
    result = chat.send_message(message)
    return result.text


def run_chat():
    chat_model = create_session()
    print(f"Chat Session Created")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break

        content = response(chat_model, user_input)
        print(f"Buzz: {content}")


if __name__ == "__main__":
    run_chat()