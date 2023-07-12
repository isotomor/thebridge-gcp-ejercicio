from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage, datastore
import json
import time

app = Flask(__name__)

# Configura la conexión a Google Cloud Storage
storage_client = storage.Client()
bucket_name = 'ejercicio_completo_gcp'  # Reemplaza con el nombre de tu bucket en Google Cloud Storage
bucket = storage_client.bucket(bucket_name)

# Configura la conexión a Datastore
datastore_client = datastore.Client()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtiene los datos ingresados en el formulario
        id = int(request.form['id'])  # Convierte el campo 'ID' a un número entero
        nombre = request.form['nombre']
        correo = request.form['correo']
        fecha = request.form['fecha']

        # Crea el objeto JSON con los datos del usuario
        usuario = {
            "ID": id,
            "Nombre": nombre,
            "Correo electrónico": correo,
            "Fecha de registro": fecha
        }

        # Genera un nombre único para el archivo JSON utilizando la fecha y hora actual
        timestamp = int(time.time())  # Obtiene la marca de tiempo actual en segundos
        file_name = f'datos_{timestamp}.json'  # Nombre del archivo JSON

        # Guarda el objeto JSON en Google Cloud Storage
        blob = bucket.blob(file_name)
        blob.upload_from_string(data=json.dumps(usuario), content_type='application/json')

        time.sleep(4)
        # Redirecciona a la misma página para recargar
        return redirect(url_for('index'))

    # Obtiene todos los usuarios de Datastore
    users = []
    query = datastore_client.query(kind='users')
    docs = query.fetch()
    for doc in docs:
        users.append(doc)

    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
