from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica para processar os dados do formulário de login, se necessário
        return redirect(url_for('agendamento'))  # Redirecionar para a página de agendamento após o login

    return render_template('login.html')

# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']
        tipo_cadastro = request.form['tipo_cadastro']

        if tipo_cadastro == 'prestador':
            tipo_servico = request.form['tipo_servico']
            # Lógica para salvar as informações do prestador no banco de dados, se necessário

            return f"Cadastro de Prestador - Nome: {nome}, CPF: {cpf}, Email: {email}, Senha: {senha}, Tipo de Cadastro: {tipo_cadastro}, Tipo de Serviço: {tipo_servico}"

        elif tipo_cadastro == 'usuario':
            # Lógica para salvar as informações do usuário no banco de dados, se necessário

            # Redirecionar para a página de login após o cadastro
            return redirect(url_for('login'))

    return render_template('cadastro.html')

# Rota de agendamento
@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        # Lógica para processar os dados do formulário de agendamento, se necessário
        return redirect(url_for('confirmacao_agendamento'))  # Redirecionar para a página de confirmação após o agendamento

    return render_template('agendamento.html')

# Rota de confirmação após o agendamento
@app.route('/confirmacao_agendamento', methods=['GET', 'POST'])
def confirmacao_agendamento():
    return render_template('confirmacao_agendamento.html')

@app.route('/avaliacao', methods=['GET', 'POST'])
def avaliacao():
    if request.method == 'POST':
        return redirect(url_for('confirmacao_avaliacao'))

    return render_template('avaliacao.html')

@app.route('/confirmacao_avaliacao')
def confirmacao_avaliacao():
    return render_template('confirmacao_avaliacao.html')


if __name__ == '__main__':
    app.run(debug=True)
