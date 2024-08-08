#Obter permissões de execução para scripts: chmod +x start_prod.sh
export ENV=production
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
