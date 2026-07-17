from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import blog_prompt

load_dotenv()
def generative_blog(topic , tone , length , audience , temperature):
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = temperature,
    )
    prompt = blog_prompt.format(
        topic = topic,
        tone = tone,
        length = length,
        audience = audience
      

    )
    response = llm.invoke(prompt)
    return response.content