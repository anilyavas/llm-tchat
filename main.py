import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

load_dotenv()

chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

human_message_template = HumanMessagePromptTemplate.from_template("{content}")

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[human_message_template],
)

chain = LLMChain(llm=chat, prompt=prompt)

while True:
    content = input(">> ")

    result = chain.run({"content": content})

    print(result)
