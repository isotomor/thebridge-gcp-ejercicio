# Utiliza una imagen base de Python con Flask instalado
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo app.py al directorio de trabajo
COPY web.py .

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Copia la carpeta templates al directorio de trabajo
COPY templates/ templates/

# Copia la carpeta static al directorio de trabajo
COPY static/ static/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 5000

# Define el comando para iniciar la aplicación
CMD ["python", "web.py"]
