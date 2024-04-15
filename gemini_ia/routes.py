from flask import render_template, request # render_template para renderizar modelos HTML e request para lidar com requisições HTTP
from gemini_ia import app
from gemini_ia.forms import FormClientes
from gemini_ia.prompt import prompt, tag
import google.generativeai as genai # Importa a biblioteca generativeai do Google

key = "AIzaSyDxCKOFr2w8dYANROHro7b828O_J8Dou98"

# Define a rota principal da aplicação, que pode lidar com os métodos GET e POST
@app.route('/', methods=["GET", "POST"])
def index(): 
    # Cria uma instância do formulário FormClientes
    form = FormClientes()
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
        # Verifica se o formulário foi validado com sucesso
        if form.validate_on_submit():
            # Obtém o briefing comercial do formulário
            briefing = form.briefing.data
            # Cria o prompt para a API de IA usando o briefing comercial
            promp = f"{tag} Briefing comercial:{briefing} {prompt}"
            # Configura a chave da API da biblioteca generativeai
            genai.configure(api_key=key)
            # Cria uma instância do modelo de IA
            model = genai.GenerativeModel('gemini-pro')
            # Gera o conteúdo com base no prompt usando o modelo de IA
            response = model.generate_content(promp)
            # Atribui a resposta da API ao campo de resposta do formulário
            form.resposta_api.data = response.text  # Atribui a resposta ao campo do formulário
    # Renderiza o template 'index.html', passando o formulário como contexto
    return render_template('index.html', form=form)