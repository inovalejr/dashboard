from flask import Flask, render_template_string
import os

app = Flask(__name__)

# O código index.html é lido aqui, não mais na rota, garantindo que ele seja lido apenas uma vez.
try:
    # Acessa o diretório atual do script Python (que deve ser a raiz do projeto)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'index.html')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        INDEX_HTML_CONTENT = f.read()
except FileNotFoundError:
    # Retorna um erro claro se o arquivo não for encontrado
    INDEX_HTML_CONTENT = "<h1>Erro: index.html não encontrado! Verifique se o arquivo está na raiz do repositório.</h1>"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_html(path):
    """Serve the index.html content for all routes."""
    # O Gunicorn/Flask serve o conteúdo estático
    # A rota principal apenas retorna o HTML lido.
    return render_template_string(INDEX_HTML_CONTENT)

if __name__ == '__main__':
    # O Gunicorn é o servidor de produção, mas usamos a.run() para testes locais.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
