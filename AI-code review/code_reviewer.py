from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import review_prompt
load_dotenv()
def review_code(language,review_type,code,temperature):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=temperature)
    prompt = review_prompt.format(language=language,review_type=review_type,code=code)
    return llm.invoke(prompt).content