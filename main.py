import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

load_dotenv()

chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
)
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)
chain = LLMChain(llm=chat, prompt=prompt, memory=memory)

while True:
    content = input(">> ")

    result = chain.run({"content": content})

    print(result)
