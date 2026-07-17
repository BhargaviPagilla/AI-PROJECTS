from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import tutor_prompt

load_dotenv()

def ask_tutor(subject,topic,difficulty,question,temp):
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=temp)
    prompt=tutor_prompt.format(subject=subject,topic=topic,difficulty=difficulty,question=question)
    return llm.invoke(prompt).content