
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

chat_history = [
    SystemMessage(content="You are a helpful AI assistant ")
]

while True:
    user_input = input('You: ')

    if user_input.lower() == 'exit':
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    print('AI:', result.content[0]['text'])

    chat_history.append(AIMessage(content=result.content))

print(chat_history)
