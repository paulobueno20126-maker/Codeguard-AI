from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega as variáveis de ambiente explicitamente do arquivo .env na mesma pasta
base_dir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# Configuração de CORS para permitir que o teu React fale com o Python sem bloqueios
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Puxa a chave do ambiente e valida se ela existe mesmo
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ ALERTA CODEGUARD: A variável GEMINI_API_KEY está vazia! Verifica o teu arquivo .env")
else:
    print(f"✅ CODEGUARD: Chave detetada com sucesso (Inicia com: {api_key[:5]})")

# Configura a chave de API no cliente oficial do Google
genai.configure(api_key=api_key)

SYSTEM_INSTRUCTIONS = (
    "Tu és o CODEGUARD AI, um Engenheiro de Software Full-Stack Sénior de Elite.\n"
    "O utilizador (Paulo) vai enviar código ou uma imagem (como um rascunho de ecrã, print de erro ou diagrama) junto com instruções.\n\n"
    "REGRAS DE EXECUÇÃO:\n"
    "1. Se houver imagem, analisa-a visualmente com extremo cuidado (elementos de interface, textos, erros).\n"
    "2. Se o utilizador pedir para EDITAR a imagem (ex: 'apaga o texto', 'aumenta a flor'), simula o comportamento lógico e descreve a alteração ou gera o código corrigido.\n"
    "3. Responde sempre em Português de Portugal, de forma direta, técnica e limpa.\n"
    "4. Quando gerar código, use blocos de código formatados em Markdown."
)

@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze_code():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    try:
        if request.content_type.startswith('multipart/form-data'):
            user_text = request.form.get('code', '')
            language = request.form.get('language', 'python')
            action = request.form.get('action', 'analyze')
            image_file = request.files.get('image')
        else:
            data = request.json or {}
            user_text = data.get('code', '')
            language = data.get('language', 'python')
            action = data.get('action', 'analyze')
            image_file = None

        if not user_text and not image_file:
            return jsonify({'error': 'Por favor, escreve alguma instrução ou envia uma foto.'}), 400

        action_upper = str(action).upper()
        prompt_final = f"[Modo Ativo: {action_upper}]\n[Linguagem Alvo: {language}]\n\nInstruções do Paulo:\n{user_text}"
        contents = [prompt_final]
        
        if image_file:
            image_bytes = image_file.read()
            mime_type = image_file.content_type
            contents.append({
                "mime_type": mime_type,
                "data": image_bytes
            })

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_INSTRUCTIONS
        )
        
        response = model.generate_content(contents)
        return jsonify({'analysis': response.text})

    except Exception as e:
        return jsonify({'error': f'Erro interno no Servidor Python: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)