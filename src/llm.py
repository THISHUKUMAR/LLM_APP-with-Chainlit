import google.generativeai as genai
from dotenv import load_dotenv
import os
from src.prompt import system_instruction

# Configure the API key
load_dotenv()
# GEMINI_API_KEY=os.environ["GEMINI_KEY"] 
# os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key='AIzaSyDkhGv3hNtK0o1NNFd7FDUAmRk0hDjUaWY')
messages = [
    {"role": "system", "content": system_instruction}
]
# Initialize the Gemini model (flash version)
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=system_instruction
    # api_key=GEMINI_API_KEY
)

def ask_order(messages, temperature=0):
    # Convert OpenAI-style messages to Gemini-friendly prompt
    formatted_conversation = ""
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            formatted_conversation += f"User: {content}\n"
        elif role == "assistant":
            formatted_conversation += f"Assistant: {content}\n"

    # Generate response from Gemini
    response = model.generate_content(
        formatted_conversation.strip(),
        generation_config={"temperature": temperature}
    )

    return response.text
