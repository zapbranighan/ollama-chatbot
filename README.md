# Yet Another Ollama Chatbot
This is a Streamlit Chatbot that uses local instance of a Ollma model.
There are only a few models you can choose from.

# Prerequisites
Have a local instance of ollama running. To download and install ollama please visit [https://ollama.com/](https://ollama.com/)
Once ollama is installed you can issue `ollama run <model>`

# How to run this application

```
# Create a virtual environment
python -m venv venv

# Activate environment (on macOs)
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the streamlit application
streamlit run chatbot.py
```