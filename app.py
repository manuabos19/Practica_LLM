import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

@st.cache_resource(show_spinner=False)
def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("./T5-finetuned")
    model = AutoModelForSeq2SeqLM.from_pretrained(
        "./T5-finetuned",
        device_map="auto",
        torch_dtype=torch.float16
    )
    return tokenizer, model

tokenizer, model = load_model_and_tokenizer()

st.title("Chatbot para resolucion de incidencias de tecnicos de EQUINSA PARKING ")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""

user_input = st.text_input("Escribe tu pregunta:")

def generar_respuesta(prompt, max_length=256, temperature=0.7, top_p=0.95):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output_ids = model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        num_return_sequences=1
    )
    response_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response_text

if st.button("Enviar"):
    prompt = f"\nUsuario: {user_input}\nChatbot:"
    output = generar_respuesta(prompt)
    if "Chatbot:" in output:
        response = output.split("Chatbot:")[-1].strip()
    else:
        response = output.strip()
    st.session_state.chat_history += f"\nUsuario: {user_input}\nChatbot: {response}"


st.text_area("Conversación", st.session_state.chat_history, height=400)
