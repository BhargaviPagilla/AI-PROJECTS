from langchain_core.prompts import PromptTemplate
review_prompt=PromptTemplate(
    input_variables=["language", "review_type","code"],
    template="""
    you are a senior software Engineer
    Review this {language} code.
    Review Type: {review_type}
    Provide:
    1. Summary
    2. Syntax Errors
    3. Logic Errors
    4. Performance Improvements
    5. Security Issues
    6. Best Practices
    7. Improved Code
    8. Explanation

    Code:
    '''{language}
    {code}
    '''
    Return Markdown.
    """)