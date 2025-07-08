# Usamos una imagen base oficial de Python ligera
FROM python:3.11-slim

# Instalamos dependencias del sistema para ibm_db y otras utilidades
RUN apt-get update && apt-get install -y \
    libxml2 \
    libxml2-dev \
    libaio1 \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la app al contenedor
COPY . /app

# Instalamos los paquetes Python (ibm_db, flask, etc) listados en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto donde correrá Flask
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app.py"]
