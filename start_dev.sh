#Obter permissões de execução para scripts: chmod +x start_dev.sh
export ENV=development
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
