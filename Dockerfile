# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala dependencias del sistema necesarias para ibm_db
RUN apt-get update && apt-get install -y \
    libxml2 \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Instala los paquetes de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto Flask
EXPOSE 8080

# Comando para correr la app
CMD ["python", "app.py"]
