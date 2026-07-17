from langchain_core.prompts import PromptTemplate

blog_prompt = PromptTemplate(
    input_variables=["topic", "tone", "length", "audience"],
    template="""
You are an expert content writer.
Write a {length} blog post.

Topic: {topic}
Tone: {tone}
Audience: {audience}

Include:
- Catchy title
- Introduction
- 4-5 headings
- Practical examples
- Key takeaways
- Conclusion

Return the response in Markdown.
"""
)
