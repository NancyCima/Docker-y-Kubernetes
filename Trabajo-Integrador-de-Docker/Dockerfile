# Usamos una imagen base oficial de Python
FROM python:3.10-slim

# Creamos un directorio para la app
WORKDIR /app

# Copiamos los archivos necesarios
COPY app/ /app/

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 8080
EXPOSE 8080

# Comando para iniciar el servidor con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
