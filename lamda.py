import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'zappanuevo'


def lambda_handler(event, context):
    # URL de la página del tiempo que quieres descargar
    url = 'https://eltiempo.com'

    # Obtener la fecha actual
    today = datetime.now().strftime('%Y-%m-%d')
    file_name = f"{today}.html"

    # Descargar la página web
    response = requests.get(url)

    if response.status_code == 200:
        # Guardar el contenido en S3
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=response.content)
        return f"Archivo {file_name} guardado con éxito en {BUCKET_NAME}."
    else:
        return f"Error al descargar la página: {response.status_code}"
