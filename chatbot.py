
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

# Create in-memory chat history
demo_ephemeral_chat_history = ChatMessageHistory()

# Add a sidebar for Ollama model selection
with st.sidebar:
    model = st.selectbox(
        "Select a model",
        ("llama3.1", "llama3", "gemma2", "mistral", "mixtral"),
    )

    st.markdown("## Notes:")
    note_text = """
You can use the model selection sidebar to select the model you want to use
Remember to run 'ollama run <model>' to start the model.
"""

    st.markdown(note_text)

st.title(f'Chat with local Ollma model: {model}')

# Create Ollama LLM
chat = OllamaLLM(model=model)

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