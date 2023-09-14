
# Construye tu propio ambiente de Data Analytics con CDK!

Hola en este repositorio encontraras la implementacion de un pequeño ambiente de Data Analytics con CDK. A continuacion te presento un diagrama de todo el ambiente final.

![ambiente](https://github.com/satencioh/cdk-demo-2023-1/assets/16481635/cd03bcc8-168f-4c81-b03c-1ffcaee976d6)

para utilizar este repositorio debes seguir los siguientes pasos:

1. Tener previamente instalado python
2. Tener previamente instalado y configurado cdk aqui te dejo documentacion de como realizarlo: https://docs.aws.amazon.com/es_es/cdk/v2/guide/getting_started.html
3. Clonar el repositorio en tu maquina local
4. estando dentro del proyecto crear un ambiente virtual asi: 

```
$ python -m venv .venv
```
5. activar el ambiente virtual
```
.venv/Scripts/activate

```
6. una vez que el entorno virtual este activado, puedes instalar las dependecias requeridas, asi:
```
$ pip install -r requirements.txt
```
7. En este punto, ahora puede sintetizar la plantilla de CloudFormation para este código.
```
$ cdk synth
```
8. y por ultimo, desplega esta pila en su cuenta/región de AWS predeterminada, asi:
```
$ cdk deploy
```
Disfruta del aprendizaje :)
