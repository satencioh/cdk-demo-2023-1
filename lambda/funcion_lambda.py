import boto3
import os

def lambda_handler(event, context):
    print('Se han encontrado {} archivo(s) nuevo(s) en el bucket'.format(len(event['Records'])))
    
    print(event)

    # Comenzamos la ejecución del crawler

    response = boto3.client('glue').start_crawler(
        Name= os.environ.get('NOMBRE_CRAWLER')
    )
    print (response)