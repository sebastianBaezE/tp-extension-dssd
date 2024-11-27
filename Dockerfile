# Imagen base
FROM python:3.10-slim

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
COPY main.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar el servicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
