# 📖 Sistema de Blog - Plataforma de Postagem de Conteúdos 📖

Bem-vindo ao **BlogX**, uma plataforma simples e intuitiva para criar, visualizar e interagir com posts de blogs! 🚀  
Este README contém todas as informações que você precisa para configurar, executar e explorar o projeto.

---

## 🎯 Funcionalidades Principais
### 🔓 Sistema de Autenticação
- Registro de usuários 📝
- Login/Logout 🔐
- Permissão baseada no usuário:
  - Apenas usuários autenticados podem comentar.
  - Apenas o autor do post ou do comentário pode excluí-los.

### 📝 Gerenciamento de Posts
- Criar novos posts 🆕
- Listar todos os posts 📋
- Visualizar detalhes de um post específico 👁️

### 💬 Interação com Comentários
- Adicionar comentários a posts 💡
- Excluir comentários indesejados (autorização necessária) ❌

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 🐍
- **Framework:** Django 🌐
- **Frontend:** HTML5, CSS3, Bootstrap 🎨
- **Banco de Dados:** SQLite 🗂️ (configuração padrão)

---

## 🚀 Passo a Passo para Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/wandeilsonfernandes/Sistema-de-Blog.git
cd Sistema-de-Blog
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install django
```

### 4️⃣ Configurar o Banco de Dados
```bash
python manage.py migrate
```

### 5️⃣ Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

### 6️⃣ Acessar o Projeto no Navegador
Abra o navegador e acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌟 Como Usar?
### 🔹 Cadastro de Usuário
1. Clique em **Registrar** na página inicial.
2. Preencha seu nome de usuário, e-mail e senha.
3. Após registrar-se, faça login.

### 🔹 Criar um Post
1. Após fazer login, clique em **Criar Post**.
2. Preencha o título e o conteúdo.
3. Clique em "Publicar".

### 🔹 Comentar em um Post
1. Acesse os detalhes de um post.
2. Escreva um comentário no campo fornecido.
3. Clique em "Enviar".

### 🔹 Excluir Posts e Comentários
- Comentários: Apenas o autor do comentário ou o autor do post pode excluí-los.

---

## 🧩 Estrutura do Projeto
```
projeto_blog/
│
├── blog/                # Aplicação principal
│   ├── migrations/      # Migrações Banco de Dados
│   ├── templates/       # Templates HTML
│   ├── admin.py/        # Painel admin
│   ├── apps.py          # Aplicações
│   ├── forms.py/        # Formulários
│   ├── models.py        # Modelos de dados
│   ├── tests.py         # Testes
│   └── urls.py          # Rotas da aplicação
│   ├── views.py         # Lógica de negócio
│
├── db.sqlite3           # Banco de Dados
├── manage.py            # Gerenciador do Django
└── requirements.txt     # Dependências do projeto
```

---

## 🛡️ Licença
Este projeto é de código aberto. Sinta-se à vontade para utilizá-lo e adaptá-lo às suas necessidades. 😊

---

## 🤝 Contribuições
Adoraríamos contar com suas contribuições! 💡  
- Crie um **fork** do repositório.
- Faça alterações no código.
- Submeta um **pull request** com suas sugestões.

---

👨‍💻 **Desenvolvido por você!** 🚀  
🎉 Obrigado por conferir o projeto! Caso tenha dúvidas, não hesite em perguntar. 😊
