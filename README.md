# Nome do Sistema

Sistema de exemplo exemplo exemplo

## Backend

## Como começar?

01. **Clonar repositório**: Clone o projeto diarias para sua máquina local.

```bash
git clone https://github.com/matheussacg/boilerplate-fastapi-postgres.git

cd projeto
```

02. **Configurar Ambiente Virtual (Opcional para DevOps)**:

- Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv

.\venv\Scripts\activate # Windows

source venv/bin/activate # macOS/Linux
```

03. **Instalar Dependências**:

- Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

04. **Criação de Token de Segurança**:

- Para gerar um token de segurança, execute o seguinte comando:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

05. **Configuração do Ambiente .env**:

- Na raiz do projeto existe um arquivo chamado `.env-exemplo` com toda estrutura feita, altere com seus dados.

- Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente necessárias:

```plaintext
# Configuração do tipo de ambiente
TIPO_AMBIENTE = 'dev'

# Configurações comuns
API_V1_STR="/api/v1"
TITLE='Sistema Base'

# Configurações de desenvolvimento (DB)
DEV_LOG_LEVEL='debug'
DEV_RELOAD='true'

# Configurações de produção (DB)
PROD_DB_USER='postgres'
PROD_DB_PASSWORD='123'
PROD_DB_HOST='localhost'
PROD_DB_PORT='5432'
PROD_DB_NAME='testedb'
PROD_LOG_LEVEL='info'
PROD_RELOAD='false'

# Configuração de email
MAIL_USERNAME='teste@teste.com.br'
MAIL_PASSWORD='teste123'
MAIL_FROM='teste@teste.com.br'

# Chave secreta token
JWT_SECRET='dfr7C9MhZojqr7ncxEB56h6klRA_5aHEEghjNFkB98'

# Link de acesso (Frontend)
LINK_ACESSO='sistemabase.teste.com.br'
```

06. **Executar a aplicação**:

- Esse comando inicia o servidor FastAPI em modo de recarregamento automático, que é útil para desenvolvimento.

```bash
python main.py
```

07. **Banco de Dados e Migrações**:

- Certifique-se de que as variáveis de ambiente relacionadas ao banco de dados estejam configuradas corretamente no arquivo `.env`.

- Verifique as migrações existentes no diretório `alembic/versions` com:

```bash
alembic current
```

- Para aplicar as migrações e atualizar o banco de dados, use:

```bash
alembic upgrade head
```

08. **Configurações de Formatação e Linting**:

#### Black - Formatação de Código

- Black é o formatador de código configurado para este projeto. Para formatar o código, execute:

```bash
black .
black .\main.py # Diretório específico
```

#### Isort - Organização de Importações

- Isort organiza as importações automaticamente. Para organizar as importações no projeto, execute:

```bash
isort .
isort .\main.py # Diretório específico
```

#### Flake8 - Linting de Código

- Flake8 é usado para garantir a qualidade do código. Para executar o linting, use:

```bash
flake8 .
flake8 .\main.py # Diretório específico
```

09. **Pre-commit**:

#### Automatização com Pre-commit

- Pre-commit é configurado para rodar Black, Isort e Flake8 antes de cada commit, garantindo que o código esteja sempre formatado e lintado.

- Para configurar o Pre-commit no projeto, execute:

```bash
pre-commit install
```

- Para rodar o Pre-commit manualmente em todos os arquivos, use:

```bash
pre-commit run --all-files
```

10. **Estrutura do Projeto**:

### Diretórios

-`app/`: Contém a aplicação principal.

-    `api/`: Diretório contendo as rotas e versões da API.
-    `core/`: Configurações centrais, como autenticação, banco de dados, etc.
-    `models/`: Define os modelos de dados e tabelas do banco de dados.
-    `schema/`: Esquemas para validação de dados usando Pydantic.
-    `services/`: Lógica de negócios e funções auxiliares usadas pelos endpoints.
-    `utils/`: Funções utilitárias usadas em várias partes do projeto.

-`migrations/`: Diretório contendo as migrações do banco de dados gerenciadas pelo Alembic.

-`test/`: Diretório para testes, dividido em:
-    `integration/`: Testes de integração.
-    `unit/`: Testes unitários.

-`venv/`: Ambiente virtual do Python (opcional).

### Arquivos principais

-   `main.py`: Ponto de entrada da aplicação.
-   `pyproject.toml`: Arquivo de configuração para ferramentas como Black, Isort, etc.
-   `.env`: Arquivo de configuração de variáveis de ambiente.
-   `requirements.txt`: Lista de dependências do Python.

## Rotas da API - V1

Este diretório contém os endpoints da API para a versão 1.

### Estrutura de Diretórios

- `api/v1/endpoints/`
- `user.py`: Endpoint com todos os métodos relacionados ao usuário.

### Endpoints `user`

#### URL: `/enviar-link-acesso` (`http://localhost:8000/api/v1/user/enviar-link-acesso`)

Descrição: Este endpoint envia um link de acesso para o sistema de diárias para o email fornecido.

- **Método HTTP**: POST
- **Parâmetros**:
  - **email**: Endereço de email do destinatário.
- **Autenticação**:
  - Não requer autenticação.
- **Validações**:
  - Apenas emails com o domínio `@fesfsus.ba.gov.br` são autorizados.
- **Exemplo de Requisição**:

````bash
curl -X POST -H "Content-Type: application/json" -d '{"email": "usuario@fesfsus.ba.gov.br"}' http://localhost:8000/api/v1/user/enviar-link-acesso
````

**Respostas**:

- **200 OK**: O email foi enviado com sucesso.

````bash
{
    "message": "Email enviado com sucesso."
}
````

**400 Bad Request**: Quando o email fornecido não está no domínio autorizado.

````bash
{
    "detail": "Apenas emails com o domínio @fesfsus.ba.gov.br são autorizados a receber o link de acesso."
}
````

#### URL: `/` (`http://localhost:8000/api/v1/user/`)

Descrição: Este endpoint cria um novo usuário no sistema.

- **Método HTTP**: POST
- **Parâmetros**:
  - **username**: Nome do usuário.
  - **email**: Endereço de email do usuário.
  - **Autenticação**:
    - Não requer autenticação.
- **Validações**:
  - `username` e `email` são obrigatórios.
- **Exemplo de Requisição**:

````bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "john_doe", "email": "john_doe@example.com"}' http://localhost:8000/api/v1/user/
````

**Respostas**:

- **201 Created**: O usuário foi criado com sucesso.

````bash
{
    "id": 1,
    "username": "john_doe",
    "email": "john_doe@example.com"
}
````

- **400 Bad Request**: Dados de entrada inválidos.

````bash
{
    "detail": "Dados inválidos."
}
````

#### URL: `/{user_id}` (`http://localhost:8000/api/v1/user/{user_id}`)

Descrição: Este endpoint retorna os detalhes de um usuário específico com base no ID.

- **Método HTTP**: GET
- **Parâmetros**:
  - **user_id**: ID do usuário.
  - **Autenticação**:
    - Não requer autenticação.
- **Exemplo de Requisição**:

````bash
curl -X GET http://localhost:8000/api/v1/user/1
````

**Respostas**:

- **200 OK**: Detalhes do usuário.

````bash
{
    "id": 1,
    "username": "john_doe",
    "email": "john_doe@example.com"
}
````

- **404 Not Found**: Usuário não encontrado.

````bash
{
    "detail": "User not found"
}
````

#### URL: `/` (`http://localhost:8000/api/v1/user/`)

Descrição: Este endpoint lista os usuários registrados no sistema.

- **Método HTTP**: GET
- **Parâmetros**:
  - **skip**: Quantidade de usuários a pular (opcional).
  - **limit**: Quantidade máxima de usuários a retornar (opcional).
  - **Autenticação**:
    - Não requer autenticação.
- **Exemplo de Requisição**:

````bash
curl -X GET http://localhost:8000/api/v1/user/?skip=0&limit=10
````

**Respostas**:

- **200 OK**: Lista de usuários.

````bash
[
    {
        "id": 1,
        "username": "john_doe",
        "email": "john_doe@example.com"
    },
    {
        "id": 2,
        "username": "jane_doe",
        "email": "jane_doe@example.com"
    }
]
````

#### URL: `/{user_id}` (`http://localhost:8000/api/v1/user/{user_id}`)

Descrição: Este endpoint atualiza os detalhes de um usuário específico com base no ID.

- **Método HTTP**: PUT
- **Parâmetros**:
  - **user_id**: ID do usuário.
  - **username**: Novo nome do usuário.
  - **email**: Novo endereço de email do usuário.
  - **Autenticação**:
    - Não requer autenticação.
- **Exemplo de Requisição**:

````bash
curl -X PUT -H "Content-Type: application/json" -d '{"username": "new_username", "email": "new_email@example.com"}' http://localhost:8000/api/v1/user/1
````

**Respostas**:

- **200 OK**: Usuário atualizado com sucesso.

````bash
{
    "id": 1,
    "username": "new_username",
    "email": "new_email@example.com"
}
````

- **404 Not Found**: Usuário não encontrado.

````bash
{
    "detail": "User not found"
}
````