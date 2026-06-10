from dotenv import load_dotenv
load_dotenv()

from ingest import load_faq_data, build_index
from rag_helper import RAGBase
from openai import OpenAI
import os

documents = load_faq_data()
index = build_index(documents)


openai_client=OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://apihub.agnes-ai.com/v1")

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)

answer = assistant.rag("What's the duration of the course?")
print(answer)

