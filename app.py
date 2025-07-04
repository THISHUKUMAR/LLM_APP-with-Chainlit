import chainlit as cl
from src.llm import ask_order, messages


@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! Welcome to Maharaj Food OrderBot 🍽️. What would you like to have today?").send()

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()
