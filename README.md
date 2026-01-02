# 🚀 Mupi Digital — Teste Técnico (Estágio Desenvolvedor Full Stack)
**Candidata:** Lorena Avelino de Oliveira  
**Vaga:** Estágio em Técnologia  
**Ano:** 2026

Este projeto foi desenvolvido como parte do **teste técnico para a vaga de Estágio em Desenvolvimento Full Stack**.

A aplicação consiste em uma **landpage pública com formulário de contato**, onde as mensagens são salvas em banco de dados, e uma **área administrativa protegida por login**, na qual é possível visualizar todas as mensagens recebidas.

---

## 📌 Visão Geral

### Funcionalidades principais

- ✅ Landpage responsiva para uma **agência de marketing digital**
- ✅ Formulário de contato funcional (nome, e-mail e mensagem)
- ✅ Mensagens salvas no banco de dados
- ✅ Feedback visual ao usuário (toast de sucesso/erro)
- ✅ Tela de **login customizada**
- ✅ **Painel administrativo protegido** por autenticação
- ✅ Listagem de mensagens ordenadas por data
- ✅ Logout funcional

---

### Funcionalidades extras (diferenciais)

Além dos requisitos obrigatórios, foram implementados alguns diferenciais com foco em
usabilidade, organização do código e experiência do usuário:

- ⭐ Feedback visual com **toasts flutuantes** (sucesso/erro), com auto-fechamento e botão de fechar
- ⭐ Layout totalmente **responsivo**, incluindo:
  - Menu mobile (hambúrguer) na landpage
  - Visualização alternativa em **cards no mobile** para o painel administrativo
- ⭐ Filtro de busca por texto no painel administrativo
- ⭐ Uso de **template base (`base.html`)** para centralizar:
  - favicon
  - TailwindCSS
  - estrutura de layout

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Django 4+**
- **Django Templates**
- **SQLite** (banco padrão do Django)
- **TailwindCSS (via CDN)** para estilização
- **HTML5**

---

## 📂 Estrutura do Projeto

```text
projeto_estagio_2026_1/
├── README.md
├── requirements.txt
├── manage.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── contato/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── landpage.html
│       ├── login.html
│       └── painel.html
└── static/
```

---


## ▶️ Como Rodar a Aplicação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/projeto_estagio_2026_1.git
cd projeto_estagio_2026_1
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
```
#### Windows
```bash
venv\Scripts\activate
```
#### Linux/Mac
```bash
source venv/bin/activate
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Criar o superusuário (admin)
```bash
python manage.py createsuperuser
```
Esse usuário será utilizado para acessar a área administrativa da aplicação.
- Escolha um nome de usuário, adicione e-mail e senha.
### 6️⃣ Executar o servidor
```bash
python manage.py runserver
```
## 🌐 Acessos da Aplicação

Após iniciar o servidor de desenvolvimento, a aplicação pode ser acessada pelos seguintes endereços:

- **Landpage (pública):**  
  `http://127.0.0.1:8000/`

- **Login:**  
  `http://127.0.0.1:8000/login/`

- **Painel Administrativo (requer autenticação):**  
  `http://127.0.0.1:8000/painel/`

## 🔐 Autenticação

- O painel administrativo é protegido com `@login_required`
- Usuários não autenticados são redirecionados para a tela de login
- O logout é realizado via POST, garantindo maior segurança

## 💡 Observações

- O foco do projeto foi **funcionalidade, organização e clareza**
- A interface foi desenvolvida de forma simples, limpa e responsiva
- O uso de Tailwind via CDN foi escolhido para agilizar o setup e evitar complexidade desnecessária

## 🤖 Uso de IA

Ferramentas de IA foram utilizadas como **apoio ao aprendizado**, entendimento da stack e organização da solução.
Todo o código foi compreendido, adaptado e é totalmente explicável.

## 📌 Considerações Finais

O projeto atende aos requisitos obrigatórios do teste técnico e inclui cuidados adicionais com UX, feedback visual e organização do código.
