# Imagem base do Python
FROM python:3.9-slim-buster

# Criação do diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY app_demo_streamlit/requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos da aplicação para o contêiner
COPY app_demo_streamlit/ .

# Define a porta que a aplicação irá utilizar
EXPOSE 8501

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "app_demo_streamlit.py"]