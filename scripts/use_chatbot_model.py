from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_intro.chatbot import chat_model


# SystemMessage tells the model how to behave
messages = [
    SystemMessage(content="You're an assistant knowledgeable about healthcare. Only answer healthcare-related questions."),
    HumanMessage(content="What is Medicaid managed care?"),
 ]

# Under the hood, chat_model makes a request to an OpenAI endpoint serving gpt-3.5-turbo-0125, and the results are returned as an AIMessage.
response = chat_model.invoke(messages)
print(response)


messages = [
    SystemMessage(content="You're an assistant knowledgeable abouthealthcare. Only answer healthcare-related questions."),
    HumanMessage(content="How do I change a tire?") # it will refuse to tell you how to change your tire (sue to SystemMessage definition)
]
response = chat_model.invoke(messages)
print(response)