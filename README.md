# 🛡️ CodeGuard AI - Painel Temático Dinâmico

O **CodeGuard AI** é um assistente de engenharia de software full-stack sénior de elite concebido para ajudar programadores a auditar, testar e analisar código em tempo real. O sistema conta com uma interface inteligível e totalmente dinâmica, que adapta as cores e logótipos do painel conforme a linguagem de programação selecionada.

---

## 🚀 Funcionalidades Principais

* **Análise Geral:** Diagnósticos rápidos de blocos de código e imagens.
* **Auditoria de Segurança:** Identificação de falhas, vulnerabilidades e potenciais fugas de dados (leaks).
* **Gerador de Testes Unitários:** Criação automatizada de testes para garantir a estabilidade do software.
* **Modo Educativo:** Explicações didáticas e detalhadas sobre conceitos de engenharia de software.
* **Leitura Visual:** Suporte para envio de capturas de ecrã (fotos) para análise de interfaces ou erros do terminal.

---

## 🛠️ Tecnologias Utilizadas

### Frontend
* **React** com **Vite** (JavaScript / JSX)
* **React Markdown** & **Remark GFM** (Para renderizar as respostas da IA com formatação rica)
* **React Syntax Highlighter** (Com tema `vscDarkPlus` para blocos de código legíveis)

### Backend
* **Python**
* **Flask** & **Flask-CORS** (Para disponibilizar a API local)
* **Google Generative AI SDK** (Integração oficial com o modelo `gemini-1.5-flash`)
* **Python-Dotenv** (Para gestão segura de credenciais locais)

---

## 📦 Como Rodar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/paulobueno20126-maker/Codeguard-AI.git](https://github.com/paulobueno20126-maker/Codeguard-AI.git)
cd Codeguard-AI

2. Configurar o Backend (Servidor Python)
Entra na pasta do Backend:

bash
cd Backend
Cria o teu ambiente virtual (.venv) e instala os pacotes necessários:

Bash
python -m venv .venv
# Ativa o ambiente (Windows)
.venv\Scripts\activate
# Instala as dependências
pip install python-dotenv google-generativeai flask flask-cors
Cria um ficheiro chamado .env baseado no Exemplo.env e coloca a tua chave de API do Google AI Studio:

Plaintext
GEMINI_API_KEY=AIzaSyAQUI_VEM_A_TUA_CHAVE_REAL
Inicia o servidor:

Bash
python app.py

3. Configurar o Frontend (Interface React)
Abre um novo terminal na raiz do projeto e entra na pasta do Frontend:

Bash
cd Frontend
Instala as dependências do ecossistema Node:

Bash
npm install
Inicia o servidor de desenvolvimento do Vite:

Bash
npm run dev
Abre o link gerado no teu navegador (normalmente http://localhost:5173) e testa o sistema!

🔒 Segurança de Credenciais
Este repositório segue rigorosamente os padrões de segurança da indústria. O arquivo real contendo as chaves de API (.env) está incluído no .gitignore local e nunca é exposto publicamente na internet.

Desenvolvido com 💻 por Paulo Bueno para o Showcase da Buildspace.
```
