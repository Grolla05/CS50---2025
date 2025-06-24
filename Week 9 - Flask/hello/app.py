from flask import Flask, render_template, request

# Atribui a variavel app a uma instância da classe Flask
# A classe Flask é a classe principal do framework Flask, que é usado para criar aplicações web
app = Flask(__name__)

# Define a route for the root URL
@app.route('/', methods=["GET", "POST"])
def index():                                                                    # Chama a função index quando a rota é acessada
    if request.method == "POST":
        name = request.form.get('name', 'World')                                    # Obtém o parâmetro 'name' do form da pagina index.html
        return render_template('greet.html', name=name)                             # Renderiza o template 'greet.html' passando o nome como variável
    else:
        return render_template('index.html')
