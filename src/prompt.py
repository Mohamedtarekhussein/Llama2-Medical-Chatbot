custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, please just say that I don't know the answer, don't try to make up
an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""