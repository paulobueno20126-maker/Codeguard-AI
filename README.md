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
