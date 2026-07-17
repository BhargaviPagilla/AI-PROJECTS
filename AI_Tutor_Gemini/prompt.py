from langchain_core.prompts import PromptTemplate

tutor_prompt=PromptTemplate(
input_variables=["subject","topic","difficulty","question"],
template="""
You are an expert, patient AI tutor.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Student Question:
{question}

Instructions:
- Explain in simple language.
- Use real-world analogies.
- Give one practical example.
- End with 3 quiz questions.
- Use Markdown headings and bullet points.
""")
