FROM python:3.9-slim

# Copiar el archivo de requisitos e instalar dependencias de Python

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define la variable de entorno PYTHONPATH
ENV PYTHONPATH=/app

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Comando por defecto para ejecutar el script de Python
CMD ["pytest", "--html=report.html"]