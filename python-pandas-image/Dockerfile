FROM ubuntu:latest

# Instala dependências para adicionar novos repositórios e o pip
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    # Agora sim instala a versão correta do Python
    apt-get install -y python3.10 python3-pip && \
    apt-get clean

# Instala o pandas
RUN python3.10 -m pip install pandas

WORKDIR /app

COPY script.py /app/script.py

CMD ["python3.10", "/app/script.py"]