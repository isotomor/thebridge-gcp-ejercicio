from google.cloud import storage
from google.cloud import datastore
import json

def function_ejercicio_gcp(event, context):
    # Obtener el nombre del archivo JSON creado en Cloud Storage
    bucket_name = 'thebridge_ej_gcp'  # Cambiar el nombre del bucket aquí
    file_name = event['name']

    # Crear una instancia del cliente de Cloud Storage
    storage_client = storage.Client()

    # Obtener el objeto JSON desde Cloud Storage
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    json_data = blob.download_as_text()

    # Convertir el JSON a un diccionario de Python
    data = json.loads(json_data)

    # Guardar los datos en Datastore
    datastore_client = datastore.Client()
    kind = 'users'  # Cambiar el nombre del tipo de entidad aquí

    # Crear una nueva entidad
    entity = datastore.Entity(datastore_client.key(kind))
    entity.update(data)

    # Guardar la entidad en Datastore
    datastore_client.put(entity)

    return 'Datos guardados en Datastore'