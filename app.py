from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página "Sobre Mim"
@app.route('/sobre-mim')
def sobre_mim():
    return render_template('sobre-mim.html')

# Rota para baixar o currículo
@app.route('/download_curriculo')
def download_curriculo():
    return send_from_directory(directory='static', filename='Curriculum_GiovannaLASouza.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    print("Index page accessed")  # Adicione esta linha
    return render_template('index.html')
