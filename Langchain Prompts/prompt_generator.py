from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """
    You are a research assistant. Your task is to summarize the given research paper in a specific style and length.
    The research paper is: {paper_input}. The explanation style is: {style_input}. The length of the explanation is: {length_input}.
    """
    ,
    input_variables = ['paper_input', 'style_input', 'length_input'],
    validate_template=True
)

template.save("prompt_template.json")