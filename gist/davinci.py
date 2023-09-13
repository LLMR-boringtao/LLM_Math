from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts import load_prompt
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

import warnings
warnings.filterwarnings("ignore")

llm  = OpenAI(model_name="text-davinci-003")

prompt = load_prompt("lc://prompts/llm_math/prompt.json")
response = llm(prompt.format(question="What is 100000 + 900000?"))
print(response)