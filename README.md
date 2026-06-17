# 🚀 LangChain + Groq Chatbot (Streamlit)

A real-time AI chatbot built using Streamlit, LangChain, and Groq LLMs. The app provides a ChatGPT-style interface with streaming responses, session-based memory, and a clean modular LangChain pipeline.

---

## 📌 Features

### 💬 Chat Interface
- ChatGPT-style UI using Streamlit
- Real-time user input using `st.chat_input`
- Message rendering using `st.chat_message`

### ⚡ LLM Capabilities
- Groq LLM integration via `ChatGroq`
- Multiple model support (llama3-8b-8192, gemma2-9b-it)
- Streaming token-by-token responses
- Clean output formatting using `StrOutputParser`

### 🧠 Conversation Handling
- Session-based chat memory using `st.session_state`
- Persistent chat history during session
- Clear chat functionality to reset conversation

### 🛠️ Developer Features
- Sidebar-based API key input
- Model selection control
- Error handling for API failures and missing keys
- Modular LangChain pipeline design

---

## 🧠 Architecture

```text
ChatPromptTemplate → ChatGroq → StrOutputParser
⚙️ How It Works
Streamlit initializes UI and session state
User enters Groq API key and selects model
Prompt template is combined with user input
LangChain chain processes input via Groq LLM
Response is streamed back token-by-token
Conversation is stored in session history
📁 Project Structure
p1/
│── main.py
│── qachatbot.py
│── pyproject.toml
│── requirements.txt
│── README.md
🧰 Tech Stack
Python 3.11+
Streamlit
LangChain
LangChain Core
LangChain Groq
Groq API
python-dotenv (optional)
pandas (optional)
▶️ Run the Project
streamlit run qachatbot.py
🧾 Prompt Design

System Prompt:

You are a helpful assistant powered by Groq. Answer clearly and precisely. If unsure, say you don't know. Avoid hallucinations.

🚧 Limitations
No persistent database memory (session-only chat)
API key must be entered manually each session
No RAG (retrieval-augmented generation)
No authentication system
Basic prompt-level safety only
🔧 Future Improvements
Add .env support for API keys
Add RAG with vector database integration
Add chat export (JSON / TXT)
Add temperature and token controls in UI
Improve error handling and retries
Deploy using Streamlit Cloud or Docker
🎯 Learning Outcomes
Streamlit chat UI development
LangChain LCEL pipeline understanding
LLM integration with Groq API
Streaming response handling
Session state management
Prompt engineering fundamentals
📄 License

This project is intended for learning and experimentation. Add a license if publishing publicly.
