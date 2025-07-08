FROM python:3.11-slim

# Instalación de dependencias del sistema para ibm_db
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2 \
    libxml2-dev \
    libaio1 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de la app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py

EXPOSE 8080

CMD ["python", "app.py"]
