from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

chat = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability. Be concise",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

demo_ephemeral_chat_history = ChatMessageHistory()

chain = prompt | chat

demo_ephemeral_chat_history.add_user_message("Translate this sentence from English to French: I love programming.")


response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})

print(response)

demo_ephemeral_chat_history.add_ai_message(response)
demo_ephemeral_chat_history.add_user_message("What did you just say?")

x = demo_ephemeral_chat_history.messages
print(x)

response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})

print(response)
