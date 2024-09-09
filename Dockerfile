
FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python básicas
RUN pip install --upgrade setuptools

# Configura o diretório de trabalho
WORKDIR /app

# Copia e instala dependências do projeto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Define o PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app/core"

# Expõe a porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
