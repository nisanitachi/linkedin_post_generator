from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="gemma2-9b-it")


#if __name__ == "__main__":
   # response = llm.invoke("Two most important ingradient in samosa are ")
   # print(response.content)




