import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate


## PAGE CONFIG

st.set_page_config(page_title="LangChain Groq Chatbot",page_icon=":robot_face:",layout="wide")



# TITLE
st.title("LangChain Groq Chatbot")
st.markdown("This is a simple chatbot built using LangChain and Groq. You can ask it questions and it will respond with answers.")


with st.sidebar: 
    st.header("Settings")
    ## API Key
    api_key=st.text_input(" Groq API Key", type="password",help="Get  your free API key from console.groq.com")


    ## MODEL SELECTION
    model_name=st.selectbox("Select Model",["llama3-8b-8192","gemma2-9b-it"],index=0,help="Select the model you want to use for the chatbot.")

    ## CLEAR BUTTON
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

## INITIALIZE CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = []


## INITIALIZE CHAT MODEL
@st.cache_resource
def get_chain(api_key,model_name):

    if not api_key:
       
        return None
    
    ## create prompt template
    prompt = ChatPromptTemplate.from_messages([

        ("system", "You are a helpful assistant powered by Groq. Answer questions clearly and precisely. If you don't know the answer, say you don't know. Do not make up answers."),
        ("user", "{question}"),
    ])

    ## initialize the chat model
    chat_model = ChatGroq(api_key=api_key, model=model_name)

    ## create chain
    chain = prompt | chat_model | StrOutputParser()
    return chain

## get the chain
chain=get_chain(api_key,model_name)

if not chain:
    st.warning("Please enter your Groq API key in the sidebar to use the chatbot.")
    st.markdown("You can get your free API key from [console.groq.com](https://console.groq.com).")
    

else:
    ## display the  previous messages from the recent sessions
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    ## user input
    if question:= st.chat_input("Ask a question"):

        ## add user message to the chat history
        st.session_state.messages.append({"role":"user","content":question})

        ## display user message in chat message container
        with st.chat_message("user"):  ## user-> streamlit function that dispplays message to the right side of the chat window
            st.write(question)

        ## get the response from the chain
        with st.chat_message("assistant"):  ## assistant-> streamlit function that dispplays message to the left side of the chat window
            message_placeholder = st.empty()
            full_response = ""


            try:

                ## stream responses from chain
                for chunk in chain.stream({"question": question}):
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")  ## display the response with a cursor
                message_placeholder.markdown(full_response)  ## display the response without a cursor
            
                # add assistant message to the chat history
                st.session_state.messages.append({"role":"assistant","content":full_response})

            except Exception as e:
                st.error(f"An error occurred: {e}")



              ## EXAMPLES
    st.markdown("### Example Questions")
    st.markdown("- What is LangChain?")
    st.markdown("- How does LangChain work?")
    st.markdown("- What are the benefits of using LangChain?")

