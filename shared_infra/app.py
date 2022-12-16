import os
import aws_cdk as cdk
from aws_cdk import (
    aws_events as events,
    aws_lambda as lambda_,
    Stack, Duration
)
from constructs import Construct


app = cdk.App()

class ResourceManagerCoreStack(Stack):
    """ Resource Manager Core Class """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rule = events.Rule(
                self, "ResourceManagerSweepStarted",
                schedule=events.Schedule.cron(
                    minute='0',
                    hour='18',
                    month='*',
                    week_day='MON-FRI',
                    year='*')
            )
        
        # Sweep Function
        #lambdaFn = lambda_.Function(
        #)
        # lambdaFn = pyLambda.PythonFunction(self, 
        #     "ResourceManager-Sweep",
        #     code=lambda_.Code.from_asset('./sweeper'),
        #     handler="sweeper.handler",
        #     timeout=Duration.seconds(300),
        #     runtime=lambda_.Runtime.PYTHON_3_9,  
        # )

ResourceManagerCoreStack(app, "ResourceManager-Shared-Infra",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()