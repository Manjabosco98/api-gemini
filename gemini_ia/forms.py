# Criação dos formularios do site
from flask_wtf import FlaskForm # Importa FlaskForm para criar formulários com Flask
from wtforms import StringField, TextAreaField, SubmitField # Importa os tipos de campos de formulário StringField, TextAreaField e SubmitField do WTForms
from wtforms.validators import DataRequired # Importa o validador DataRequired do WTForms para validar campos de formulário

# Define uma classe para o formulário de clientes que herda de FlaskForm
class FormClientes(FlaskForm):
    # Define um campo de texto para o briefing comercial com validação de dados obrigatórios
    briefing = StringField("Briefing Comercial", validators=[DataRequired()])
    # Define um botão de envio para o formulário
    botao_confirmacao = SubmitField("Enviar")
    # Define um campo de texto grande para exibir a resposta da API, tornando-o somente leitura
    resposta_api = TextAreaField("Resposta da API", render_kw={"readonly": True})  # Campo somente leitura