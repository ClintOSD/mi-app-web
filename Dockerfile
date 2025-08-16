# Usa una imagen base de Python 3.9
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 5000, que es donde se ejecutará la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicia el contenedor
CMD ["python", "app.py"]
