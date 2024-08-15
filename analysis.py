from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import SimpleSequentialChain
import google.generativeai as genai

def configure_gemini(api_key):
    genai.configure(api_key=api_key)

def answer_question(prompt):
    response = genai.generate_text(prompt=prompt)
    return response.result

def analyze_financial_data(financial_data):
    template = """
    Analyze the following financial data and provide detailed insights:
    {financial_data}
    """

    prompt_template = PromptTemplate(template=template, input_variables=["financial_data"])
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    insights = chain.run(financial_data=financial_data)
    return insights

def answer_complex_question(prompt):
    chain1 = LLMChain(llm=OpenAI(), prompt=PromptTemplate(template="Extract key financial metrics from the following text: {text}"))
    chain2 = LLMChain(llm=OpenAI(), prompt=PromptTemplate(template="Based on these metrics, what are the insights? {metrics}"))
    complex_chain = SimpleSequentialChain(chains=[chain1, chain2])
    response = complex_chain.run(text=prompt)
    return response.result
