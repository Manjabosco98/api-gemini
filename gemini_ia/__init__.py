# Importando bibliotecas
from flask import Flask

# Criando site
app = Flask(__name__) # Cria uma instância da aplicação Flask
app.secret_key = '04b49f7c740b5763f9a4b79ad07623e0' # Define a chave secreta para a aplicação Flask

from gemini_ia import routes