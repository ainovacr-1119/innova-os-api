FROM python:3.11-slim

WORKDIR /app

# Copia el archivo de dependencias primero
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la app
COPY . .

# Variables de entorno (Cloud Run detecta $PORT automáticamente)
ENV PORT 8080

# Comando para ejecutar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
