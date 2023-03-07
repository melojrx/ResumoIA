import streamlit as st
import openai 
import os


# Lê a chave da API da variável de ambiente
openai.api_key = "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"

# Define o título da página
st.title("Resumo de Texto com ChatGPT")

# Cria um campo de texto para inserir o texto
texto = st.text_area("Insira o texto para resumir", height=300)

# Cria um campo de número para inserir o número máximo de tokens
max_tokens = st.number_input("Número máximo de tokens no resumo", min_value=1, max_value=300, value=200)

# Define as engines que serão testadas
engine = "text-davinci-003"

# Função para gerar o resumo
def gerar_resumo(texto, max_tokens, engine):
    completions = openai.Completion.create(
        engine=engine,
        prompt=f"Escreva um resumo criativo em lingua portuguesa para o seguinte texto:\n{texto}\nResumo:",
        max_tokens=max_tokens,
        n=1,
        stop=[".", "?", "!"],
        temperature=0.2,
    )
    mensagem = completions.choices[0].text.strip()
    if mensagem[-1] not in [".", "!", "?"]:
            mensagem += "."
    return mensagem

# Cria um botão para resumir o texto
if st.button("Resumir"):
    # Gera o resumo usando a engine definida
    resumo = gerar_resumo(texto, max_tokens=max_tokens, engine=engine)
    st.write("Resumo:")
    st.write(resumo)

# Adiciona a barra lateral com informações do autor
st.sidebar.markdown("<h3 style='text-align: center; font-size: 20px; color: Red'>By Melo Jr &reg - 2023</h3>", unsafe_allow_html=True)