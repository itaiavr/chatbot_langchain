import dotenv
from langchain_openai import ChatOpenAI
"""
Core component of LangChain is the LLM.
LangChain provides a modular interface for working with LLM providers such as OpenAI, Cohere, HuggingFace, Anthropic, Together AI, and others
We need API key from the LLM provider to get started using the LLM with LangChain.
We’ll use OpenAI
We can always test out different providers and optimize depending on the application’s needs and cost constraints.

Chat models use LLMs under the hood, but they’re designed for conversations, and they interface with chat messages rather than raw text.
Using chat messages, you provide an LLM with additional detail about the kind of message you’re sending.
All messages have role and content properties.
The role tells the LLM who is sending the message, and the content is the message itself.
most commonly used messages:
HumanMessage: A message from the user interacting with the language model.
AIMessage: A message from the language model.
SystemMessage: A message that tells the language model how to behave. Not all providers support the SystemMessage.
"""


dotenv.load_dotenv()
# instantiate an OpenAI chat models in LangChain:
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
