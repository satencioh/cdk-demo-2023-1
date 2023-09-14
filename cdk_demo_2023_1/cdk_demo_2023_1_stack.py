from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_s3 as s3,
    aws_s3_notifications,
    aws_glue_alpha as glue,
    aws_glue,
    aws_iam as iam,
)
from constructs import Construct

STACK_NAME = 'CDK-ANALYTICS-2023' # Se establece el nombre de la pila
S3_RAW_PREFIX = ''

LAMBDA_CONFIG= dict (
    timeout=Duration.seconds(20),    
    memory_size=128, 
    tracing= aws_lambda.Tracing.ACTIVE, 
    runtime = aws_lambda.Runtime.PYTHON_3_8) 

class CdkDemo20231Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #bucekt que contiene los archivos de entrada
        bucket_entrada = s3.Bucket(self,"input_files")

        #creacion de la funcion lambda que se dispara cuando llega un nuevo archivo al bucket

        archivo_nuevo_lambda = aws_lambda.Function (
            self,"lambda_nuevo_archivo", 
            function_name=f"lambda_nuevo_archivo-{STACK_NAME}",
            handler='funcion_lambda.lambda_handler',
            code=aws_lambda.Code.from_asset("./lambda/"),
            **LAMBDA_CONFIG,environment={}
        )

        # creamos el objeto de notificaciones de eventos
        nuevo_objecto = aws_s3_notifications.LambdaDestination(archivo_nuevo_lambda)

        # Se agrega la noti al bucket para que invoque la lambda cuando haya un nuevo objeto
        bucket_entrada.add_event_notification(s3.EventType.OBJECT_CREATED, nuevo_objecto)

        #*********** DB GLUE Y CRAWLER *****************

        bd_glue = glue.Database(self, "demo-db-cdk", database_name="bd-analytics")

        statement = iam.PolicyStatement( actions=["s3:GetObject","s3:PutObject"],
            resources=[
                "arn:aws:s3:::{}".format(bucket_entrada.bucket_name),
                "arn:aws:s3:::{}/*".format(bucket_entrada.bucket_name)])
        
        rol_glue = iam.Role(
                self,  'crawler', role_name = 'CrawlerDemoCDK',
                assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
                managed_policies = [ iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')]
            )
        
        rol_glue.add_to_policy(statement)

        #creacion del crawler que escaneara los datos que lleguen al bucket
        crawler_glue = aws_glue.CfnCrawler(
            self, 'crawler-cdk', description="rastreador para nuevos datos raw",
            name=f'crawler-cdk-{STACK_NAME}',
            database_name=bd_glue.database_name,
            schedule=None,
            role=rol_glue.role_arn,
            table_prefix="cdk-",
            targets={"s3Targets": [{"path": "s3://{}/{}".format(bucket_entrada.bucket_name, S3_RAW_PREFIX)}]}
        )

        #le asignamos a la variable de entorno de la lambda el nombre del crawler
        archivo_nuevo_lambda.add_environment("NOMBRE_CRAWLER", crawler_glue.name)

        archivo_nuevo_lambda.add_to_role_policy(iam.PolicyStatement(actions=["glue:StartCrawler"], resources=["*"]))




