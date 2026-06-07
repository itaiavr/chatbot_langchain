# Build an LLM RAG Chatbot With LangChain

---

### Project Setup:
- go to github and create project: chatbot_langchain
- local:
- uv init chatbot_langchain  
- cd chatbot_langchain
- source .venv/bin/activate
- git init
- git checkout -b main
- git remote add origin https://github.com/your-username/your-repo-name.git
- git add .
- git commit -m "initial commit: uv project setup"
- git push -u origin main

---


The most popular ways to create an LLM-powered chatbot is through retrieval-augmented generation (RAG) 
When you design a RAG system, you use a retrieval model to retrieve relevant information,  
usually from a database or corpus, and provide this retrieved information to an LLM to generate contextually relevant responses.  
https://realpython.com/build-llm-rag-chatbot-with-langchain/


---

### About this Project:
AI engineer working for a large hospital system.
a RAG chatbot in LangChain that uses Neo4j to retrieve data about: 
- the patients 
- patient experiences, 
- hospital locations, 
- visits, 
- insurance payers, 
- physicians in hospital system.

In this project, we’ll learn how to:
- Use LangChain to build custom chatbots
- Design a chatbot using your understanding of the business requirements and hospital system data
- Work with graph databases
- Set up a Neo4j AuraDB instance
- Build a RAG chatbot that retrieves both structured and unstructured data from Neo4j
- Deploy your chatbot with FastAPI and Streamlit

We’ll have a REST API that serves your LangChain chatbot.  
We’ll also have a Streamlit app that provides a nice chat interface to interact with the API  
Under the hood:  
The Streamlit app sends messages to the chatbot API,  
The chatbot generates and sends a response back to the Streamlit app, which displays it to the user. 

Concepts and technologies: 
Large language models (LLMs) and prompt engineering  
Text embeddings and vector databases  
Graph databases and Neo4j.  
The OpenAI developer ecosystem  
REST APIs and FastAPI.  
Asynchronous programming  
Docker and Docker Compose


### Project Structure:
- langchain_intro/ : will help you get familiar with LangChain and equip you with the tools that you need to build the chatbot  
- data/ : has the raw hospital system data stored as CSV files. You’ll explore this data in Step 2.  
  In Step 3, you’ll move this data into a Neo4j database that your chatbot will query to answer questions. 
- hospital_neo4j_etl/ : contains a script that loads the raw data from data/ into your Neo4j database.   
  You have to run this before building your chatbot, and you’ll learn everything you need to know about setting up a Neo4j instance in Step 3.
- chatbot_api/ :  is FastAPI app that serves our chatbot as a REST endpoint, and it’s the core deliverable of this project.  
  The chatbot_api/src/agents/ and chatbot_api/src/chains/ subdirectories contain the LangChain objects that comprise our chatbot.  
  We’ll learn what agents and chains are later, but for now, the chatbot is actually a LangChain agent composed of chains and functions. 
- tests/ : includes two scripts that test how fast the chatbot can answer a series of questions.  
  This will give a feel for how much time you save by making asynchronous requests to LLM providers like OpenAI.
- chatbot_frontend/ : is a Streamlit app that interacts with the chatbot endpoint in chatbot_api/.  
  This is the UI that we saw in the demo, and you’ll build this in Step 5.

All the environment variables needed to build and run the chatbot will be stored in a .env file.
We’ll deploy the code in hospital_neo4j_etl/, chatbot_api, and chatbot_frontend as Docker containers that’ll be orchestrated with Docker Compose.

