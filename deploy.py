import subprocess
import os

# Caminho para a pasta do repositório Git
REPO_DIR = os.getcwd()

# Caminho para a pasta do docker-compose.yml
DOCKER_COMPOSE_DIR = REPO_DIR

# Nome da imagem e do container Docker
IMAGE_NAME = "genesis"
CONTAINER_NAME = "app-backend"


def run_command(command, cwd=None):
    """Executa um comando shell e imprime a saída."""
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        print(f"Erro ao executar comando: {command}")
        print(result.stderr)
    else:
        print(result.stdout)


def git_pull():
    """Atualiza o repositório Git."""
    print(f"Atualizando o repositório Git na pasta {REPO_DIR}")
    run_command("git pull", cwd=REPO_DIR)


def remove_image():
    """Remove a imagem Docker."""
    print(f"Removendo a imagem Docker {IMAGE_NAME}")
    run_command(f"sudo docker rmi {IMAGE_NAME} -f")


def remove_container():
    """Remove o container Docker."""
    print(f"Removendo o container Docker {CONTAINER_NAME}")
    run_command(f"sudo docker rm {CONTAINER_NAME} -f")


def start_docker_compose():
    """Inicia o docker-compose."""
    print("Iniciando o docker-compose")
    run_command("sudo docker-compose up -d", cwd=DOCKER_COMPOSE_DIR)


def run_alembic_upgrade():
    """Executa o comando alembic upgrade head dentro do container Docker."""
    print(f"Executando alembic upgrade head no container {CONTAINER_NAME}")
    command = f"sudo docker exec {CONTAINER_NAME} alembic upgrade head"
    run_command(command)


def main():
    git_pull()
    remove_container()
    remove_image()
    start_docker_compose()
    # Aguarde o Docker Compose iniciar o container e garantir que está pronto
    print("Aguardando o container iniciar...")
    import time

    time.sleep(10)  # Ajuste o tempo de espera conforme necessário
    run_alembic_upgrade()
    print("Script concluído com sucesso!")


if __name__ == "__main__":
    main()
