import gradio as gr
from ctransformers import AutoModelForCausalLM
from langchain_core.prompts import PromptTemplate
import os

model_path=os.path.join(os.getcwd(),'llama-2-7b-chat.ggmlv3.q3_K_L.bin')

if os.path.isfile(model_path):
    llm = AutoModelForCausalLM.from_pretrained(model_path_or_repo_id=model_path,local_files_only=True,model_type='llama')

    # Define the tutor role prompt
    template = """
    You are an expert tutor with a friendly and patient teaching style. Your goal is to explain concepts clearly, concisely, and in an engaging way, tailored to the student's current level of understanding. Use simple language for beginners or more technical detail for advanced learners, based on the context. Break down complex ideas into step-by-step explanations, include practical examples or analogies when helpful, and anticipate potential follow-up questions. If the student's question is unclear, ask for clarification politely before proceeding.


    Student's Request: {question}

    Your Response:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])


    def stream_response(message, history):
      response=""
      prompt_with_message=prompt.format(question=message)
      for text in llm(prompt_with_message, stream=True,max_new_tokens=500):
        response += text
        yield response

    gr.ChatInterface(
        fn=stream_response,
        type="messages",
        save_history=True,
        show_progress='full'
    ).launch(debug=True,share=True)
else:
    raise FileNotFoundError('Model file is not found. download the model file before run the application')
