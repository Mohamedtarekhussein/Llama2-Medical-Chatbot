from prompt import custom_prompt_template
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector store
    """
    prompt = PromptTemplate(
        template=custom_prompt_template,
        input_variables=['context', 'question']  
    )
    return prompt

def load_llm():
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
    )
    return llm