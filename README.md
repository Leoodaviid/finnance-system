```react
finance_system/
│
├── app.py                   # Arquivo principal do Flask, inicializa a aplicação e carrega as configurações.
├── auth.py                  # Módulo que gerencia as rotas de autenticação, incluindo login, logout e registro.
├── config.py                # Configuração para diferentes ambientes (desenvolvimento, teste, produção).
├── extensions.py            # Define e inicializa extensões Flask, como o Limiter para rate limiting.
├── models.py                # Definição dos modelos de dados usando SQLAlchemy, como User e Transaction.
├── forms.py                 # Definição dos formulários usando Flask-WTF, incluindo formulários de login, registro e transação.
├── routes.py                # Rotas da aplicação que gerenciam as operações principais, como listagem e manipulação de transações.
├── templates/               # Templates HTML (Jinja2) para a renderização das páginas da aplicação.
│   ├── base.html            # Template base que define a estrutura comum a todas as páginas.
│   ├── index.html           # Página inicial que lista as transações.
│   ├── transaction_create.html  # Página para criação de novas transações.
│   ├── transaction_edit.html    # Página para edição de transações existentes.
│   ├── transaction_report.html  # Página de relatório financeiro, exibindo receitas, despesas e saldo.
│   ├── user_create.html     # Página de registro de novos usuários.
│   ├── user_login.html      # Página de login de usuários.
├── static/                  # Arquivos estáticos (CSS, JS, imagens).
│   ├── css/                 # Pasta contendo arquivos de estilo CSS.
│   │   └── styles.css       # Estilos customizados para a aplicação.
│   └── js/                  # Pasta contendo arquivos JavaScript.
│       └── main.js          # Scripts JavaScript para manipulação de eventos e interações da interface.
└── config.py                # Configurações da aplicação para diferentes ambientes.

```

### Executando o Sistema

1. **Verifique a versão do Python instalada:**

   No terminal ou prompt de comando, execute:

   ```
   bash
   Copiar código
   python --version
   ```

   ou

   ```
   bash
   Copiar código
   python3 --version
   ```

   Você deve ver algo como `Python 3.x.x`.

2. **Criando um ambiente virtual (opcional, mas recomendado):**

   Para isolar suas dependências, é uma boa prática criar um ambiente virtual:

   ```
   python3 -m venv venv
   ```
   
   Ative o ambiente virtual:

   - No Windows:

     ```
     bash
     Copiar código
     venv\Scripts\activate
     ```
   
   - No macOS/Linux:

     ```
     source venv/bin/activate
     ```
   
3. **Instale as dependências necessárias:**

   Após ativar o ambiente virtual (se você criou um), instale as dependências:

   ```
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   Agora, execute o arquivo `app.py`:

   ```
   python3 app.py
   ```

