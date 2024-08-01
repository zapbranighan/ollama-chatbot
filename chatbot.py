
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

st.title("Chat with llama3.1")

chat = OllamaLLM(model="llama3.1")

# Create a simple chat prompt
chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability. Be concise",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Create a prompt and llm chain
chain = chat_prompt | chat

# Create in-memory chat history
demo_ephemeral_chat_history = ChatMessageHistory()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Add message to chat history
        if message["role"] == "assistant":
            demo_ephemeral_chat_history.add_ai_message(message["content"])
        else:
            demo_ephemeral_chat_history.add_user_message(message["content"])

# Display and get chat input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Add user prompt/question to chat history
    demo_ephemeral_chat_history.add_user_message(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Submit question/prompt to LLM, along with chat history
        chat_response = chain.invoke({"messages": demo_ephemeral_chat_history.messages})
        st.markdown(chat_response)

    # Add chat response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chat_response})
    demo_ephemeral_chat_history.add_ai_message(chat_response)