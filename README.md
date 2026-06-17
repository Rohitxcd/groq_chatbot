# LangChain + Groq Chatbot (Streamlit)

I built a simple, real-time AI chatbot using Streamlit for the UI, LangChain for prompt/model chaining, and Groq as the LLM provider.

The app lets users:
- Enter a Groq API key from the sidebar
- Choose a model (`llama3-8b-8192` or `gemma2-9b-it`)
- Ask questions in a chat interface
- See streaming responses token-by-token
- Keep conversation history in the current Streamlit session
- Clear chat with one click

## Project Overview

The core goal of this project is to build a beginner-friendly QA chatbot using a clean architecture:
- UI layer: Streamlit (`st.chat_input`, `st.chat_message`, sidebar controls)
- Prompt layer: `ChatPromptTemplate` with a system instruction + user question
- Model layer: `ChatGroq`
- Output layer: `StrOutputParser`

The chain is:

```text
ChatPromptTemplate -> ChatGroq -> StrOutputParser
```

This keeps the code modular and easy to extend (for example, adding memory, retrieval, tools, or a system prompt editor later).

## How I built this project (Step-by-Step)

1. I created a Streamlit app shell
- I set the page config and title
- I added a sidebar for API key and model selection

2. I added session-based chat memory
- I used `st.session_state.messages` to persist messages across Streamlit reruns
- I added a `Clear Chat` button to reset conversation state

3. I built an LLM chain function
- I wrote `get_chain(api_key, model_name)` and decorated it with `@st.cache_resource`
- I defined a prompt template with:
	- a system instruction (assistant behavior)
	- a user placeholder (`{question}`)
- I initialized `ChatGroq`
- I composed prompt + model + parser into one chain

4. I added chat display and user input
- I rendered previous messages with `st.chat_message`
- I captured the user question with `st.chat_input`
- I appended the user text to session history

5. I added streaming assistant output
- I used `chain.stream({"question": question})`
- I rendered incremental output with a cursor effect (`▌`)
- I saved the final assistant response to session history

6. I added error handling and guidance
- I wrapped the model call in `try/except`
- I displayed a warning if the API key is missing
- I added example questions for first-time users

## Current Folder Structure

```text
p1/
	main.py
	pyproject.toml
	qachatbot.py
	README.md
	requirements.txt
```

Main app file:
- `qachatbot.py`

## Tech Stack

- Python 3.11+
- Streamlit
- LangChain
- LangChain Core
- LangChain Groq

From `pyproject.toml`, the project also includes:
- `langgraph`
- `python-dotenv`
- `pandas`
- `ipykernel`

## Prerequisites

Before running the app:
- Install Python 3.11 or newer
- Create a Groq account
- Generate a Groq API key from `https://console.groq.com`

## Installation

You can install dependencies using either `requirements.txt` or `pyproject.toml`.

### Option A: Using requirements.txt

```bash
pip install -r requirements.txt
```

### Option B: Using pyproject.toml (recommended for project-based workflow)

```bash
pip install .
```

## Run the App

From the project folder:

```bash
streamlit run qachatbot.py
```

Then in the browser:
1. Paste your Groq API key in the sidebar
2. Pick a model
3. Ask a question in the chat input

## How the Chat Flow Works

1. App starts and initializes empty `st.session_state.messages` if needed
2. Sidebar collects API key and model
3. `get_chain` builds and caches the chain
4. Existing messages are rendered
5. New user input is captured with `st.chat_input`
6. User message is added to history
7. Assistant response is streamed and displayed
8. Final assistant message is saved to history

## Prompt Design

Current system prompt:

"You are a helpful assistant powered by Groq. Answer questions clearly and precisely. If you don't know the answer, say you don't know. Do not make up answers."

Why this prompt works:
- Encourages concise, accurate responses
- Reduces hallucinations by explicitly allowing "I don't know"
- Suitable for a beginner QA chatbot

## Features Implemented

- Sidebar API key input
- Model switching
- Chat history rendering
- Streaming generation
- Cursor-like typing effect
- Clear chat button
- Basic exception handling
- Example starter questions

## Known Limitations

- Conversation history is session-only (not saved to disk/database)
- API key is manually entered each run
- No retrieval (RAG), so answers depend on model knowledge only
- No multi-user auth
- Minimal guardrails beyond system prompt

## Troubleshooting

### App says API key is missing
- Ensure you pasted a valid key in the sidebar
- Confirm the key is active in Groq console

### `streamlit` command not found
- Install Streamlit: `pip install streamlit`
- Ensure your virtual environment is activated

### Model call fails
- Check internet connection
- Verify model name is valid
- Confirm Groq service/key quota is available

### Old responses still visible
- Click `Clear Chat` to reset `st.session_state.messages`

## Suggested Next Improvements

1. Add `.env` support so API key can be loaded automatically
2. Add chat export (download conversation as text/JSON)
3. Add model parameters (temperature, max tokens) in sidebar
4. Add retry and timeout handling for robustness
5. Add RAG with a vector store for domain-specific QA
6. Add tests for prompt-chain initialization and UI logic

## Learning Outcomes from This Project

By building this project, I practiced:
- Streamlit chat UI patterns
- LangChain chain composition
- LLM streaming response rendering
- Session-state based message memory
- Basic prompt engineering and error handling

## License

Use this project for learning and personal experimentation. Add a formal OSS license file (`LICENSE`) if you plan to publish publicly.
