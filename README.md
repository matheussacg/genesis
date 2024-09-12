# Nome do Sistema

[Nome do Sistema - Boilerplate Fastapi/Postgres/Alembic/Sqladmin/Docker]

## Backend

### Como começar?

## 01. **Clonar repositório**: Clone o projeto diarias para sua máquina local.

```bash
# Clone HTTPS
git clone https://github.com/matheussacg/boilerplate-fastapi-postgres.git nome_do_projeto

# Clone SSH
git clone git@github.com:matheussacg/boilerplate-fastapi-postgres.git nome_do_projeto

cd nome_do_projeto
```

## 02. **Configurar Ambiente Virtual (Opcional para ambiente local)**:

- Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv

.\venv\Scripts\activate # Windows

source venv/bin/activate # macOS/Linux
```

## 03. **Instalar Dependências (Opcional para ambiente local)**:

- Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## 04. **Criação de Token de Segurança**:

- Para gerar um token de segurança, execute o seguinte comando:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## 05. **Configuração do Ambiente .env**:

- Na raiz do projeto existe um arquivo chamado `.env-example` com toda estrutura feita, altere com seus dados.

- Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente necessárias:

Você também pode clonar o arquivo `.env-example` com o comando abaixo:

```bash
cp .env_example .env
```

```plaintext
# Configuração do tipo de ambiente
TIPO_AMBIENTE=prod

# Configurações comuns
API_V1_STR=/api/v1
TITLE=Sistema Base

# Configurações de desenvolvimento (DB)
DEV_LOG_LEVEL=debug
DEV_RELOAD=true

# Configurações de produção (DB)
PROD_DB_USER=postgres
PROD_DB_PASSWORD=1234
PROD_DB_HOST=postgres-db
PROD_DB_PORT=5432
PROD_DB_NAME=testedb
PROD_LOG_LEVEL=info
PROD_RELOAD=false

# Configuração de email
MAIL_USERNAME=teste@teste.com.br
MAIL_PASSWORD=teste123
MAIL_FROM=teste@teste.com.br

# Chave secreta token
JWT_SECRET=gfhfh9MhZojq567ncxEBghghlRA_5aHEELngSghg

# Link de acesso (Frontend)
LINK_ACESSO=sistemabase.teste.com.br
```

## 06. **Executar a aplicação**:

- A aplicação é inicializada de acordo com a configuração definida na variável TIPO_AMBIENTE no arquivo .env. Dependendo do valor atribuído, o sistema será executado em modo de desenvolvimento ou produção, com as configurações correspondentes:

```bash
TIPO_AMBIENTE='dev'
# Inicia a aplicação utilizando SQLite (sqlite+aiosqlite) com configurações voltadas para o ambiente de desenvolvimento.
```

```bash
TIPO_AMBIENTE='prod'
# Inicia a aplicação utilizando PostgreSQL (postgresql+asyncpg) com configurações de produção.
```

#### Notas:

- Em modo dev, a aplicação utilizará o banco de dados SQLite, ideal para desenvolvimento e testes rápidos.
- Em modo prod, a aplicação conectará ao banco de dados PostgreSQL utilizando as credenciais e informações definidas nas variáveis de - ambiente correspondentes (PROD_DB_NAME, PROD_DB_USER, etc.).
- Caso alguma variável de ambiente necessária para o ambiente de produção não esteja configurada corretamente, a aplicação irá gerar um erro indicando a ausência de valores obrigatórios.

```bash
python main.py
```

## 07. **Executando o ambiente com Docker**:

#### Descrição

- Este projeto utiliza Docker para configurar e executar o ambiente de desenvolvimento de forma rápida e fácil. Siga os passos abaixo para inicializar o projeto:

#### Pré-requisitos

- Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina:

```plaintext
Docker

Docker Compose
```

#### Passo a Passo para Executar o Projeto

- 1- Clone o repositório do projeto

  Primeiro, clone o repositório do projeto para o seu ambiente local:

  ```bash
  docker-compose build
  ```

- 2- Inicie os containers

  Após a construção, inicie os containers com o seguinte comando:

  ```bash
  docker-compose up
  ```

  Este comando irá iniciar todos os serviços definidos no docker-compose.yml.

- 3- Acessando a aplicação

  Uma vez que os containers estejam rodando, acesse a aplicação através do endereço configurado (http://localhost:PORTA). A porta exata pode ser encontrada no seu arquivo docker-compose.yml.

- 4- Parando os containers

  Para parar os containers, utilize o comando:

  ```bash
  docker-compose down
  ```

  Este comando irá parar e remover todos os containers criados, liberando os recursos do sistema.

- 5- Comandos Úteis

  #### Reconstruir a aplicação após alterações:

  Se fizer mudanças no `Dockerfile` ou nas configurações do projeto, reconstrua os containers com:

  ```bash
  docker-compose up --build
  ```

  #### Acessar o terminal de um container em execução:

  Para entrar no shell de um container específico, use:

  ```bash
  docker exec -it <NOME_DO_CONTAINER> /bin/bash
  ```

## 08. **Banco de Dados e Migrações**:

- Certifique-se de que as variáveis de ambiente relacionadas ao banco de dados estejam configuradas corretamente no arquivo `.env`.

- Verifique as migrações existentes no diretório `alembic/versions` com:

```bash
alembic current
```

- Para aplicar as migrações e atualizar o banco de dados, use:

```bash
alembic upgrade head
```

## 09. **Configurações de Formatação e Linting**:

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

## 10. **Pre-commit**:

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

## 11. **SQLAdmin - Painel Administrativo do Sistema**:

O projeto utiliza o SQLAdmin para gerenciar o painel administrativo, permitindo a visualização e edição dos dados através de uma interface amigável.

#### Acessando o Painel Administrativo

Após iniciar o projeto conforme as instruções da seção de execução com Docker, você pode acessar o painel administrativo do SQLAdmin no seguinte endereço:

  - URL do Painel: http://localhost:8000/admin

#### Configuração do SQLAdmin

O SQLAdmin já vem configurado com o FastAPI para facilitar a administração dos modelos do banco de dados. Para personalizar o painel, você pode ajustar as configurações no arquivo responsável pela integração do SQLAdmin `(app/core/admin.py)`.

#### Funcionalidades Disponíveis no Painel

- 1. Visualização de Dados: Permite consultar registros das tabelas do banco de dados de forma fácil e intuitiva.
- 2. Criação de Registros: Adicione novos registros diretamente pelo painel, preenchendo os campos necessários.
- 3. Edição de Registros: Atualize informações de qualquer registro existente através do painel.
- 4. Exclusão de Registros: Remova registros do banco de dados com segurança usando o painel.

#### Customização do Painel

Para ajustar os modelos e suas exibições no painel, edite o arquivo onde o SQLAdmin foi configurado `(app/core/admin.py)`. Você pode personalizar quais campos são exibidos, adicionar validações e definir permissões específicas para cada tabela.

Para mais detalhes confira a documentação completa do projeto: `https://aminalaee.dev/sqladmin/`

#### Segurança

Certifique-se de proteger o acesso ao painel administrativo. Adicione autenticação e autorização para garantir que apenas usuários autorizados possam visualizar e modificar os dados.

#### Comandos Úteis

- Reiniciar o servidor: Caso faça alterações na configuração do SQLAdmin, reinicie o servidor com:

Usando o docker:
```bash
docker-compose restart
```

Local:
```bash
python main.py
```

## 12. **Estrutura do Projeto**:

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

#### Enviar email com link de acesso

#### URL: `/enviar-link-acesso` (http://localhost:8000/api/v1/user/enviar-link-acesso)

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
curl -X POST -H "Content-Type: application/json" -d '{"email": "usuario@teste.com.br"}' http://localhost:8000/api/v1/user/enviar-link-acesso
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

#### Post para criar usuário

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

#### Get para retornar um usuário específico

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

#### Get para retornar todos os usuários

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

#### Put para editar um usuário específico

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