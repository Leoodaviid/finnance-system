```react
finance_system/
│
├── app.py                   # Arquivo principal do Flask
├── models.py                # Definição dos modelos de dados (ORM)
├── forms.py                 # Definição dos formulários (Flask-WTF)
├── routes.py                # Rotas da aplicação
├── templates/               # Templates HTML (Jinja2)
│   ├── base.html            # Template base para reutilização de layout
│   ├── index.html           # Página inicial
│   ├── register.html        # Página de registro de entradas e saídas
│   ├── report.html          # Página de relatórios financeiros
├── static/                  # Arquivos estáticos (CSS, JS, imagens)
│   └── styles.css           # Estilos customizados
├── finance.db               # Banco de dados SQLite
└── config.py                # Configurações da aplicação

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
   bash
   Copiar código
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
     bash
     Copiar código
     source venv/bin/activate
     ```

3. **Instale as dependências necessárias:**

   Após ativar o ambiente virtual (se você criou um), instale as dependências:

   ```
   bash
   Copiar código
   pip install flask flask_sqlalchemy flask_wtf
   ```

4. **Execute a aplicação:**

   Agora, execute o arquivo `app.py`:

   ```
   bash
   Copiar código
   python3 app.py
   ```

