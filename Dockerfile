# Usar uma imagem base do Python
FROM python:3.11

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expôr a porta 8000 (Django)
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]