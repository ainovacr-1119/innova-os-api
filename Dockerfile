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
<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
>>>>>>> 767f92e4f6e8c95cd86e5284b231d4bbf01eff38
