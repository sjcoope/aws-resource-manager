import os
import aws_cdk as cdk
from aws_cdk import (
    aws_events as events,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    Stack, Duration
)
from constructs import Construct
dirname = os.path.dirname(__file__)

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

        lambdaFn = lambda_.Function(self,
            "ResourceManager-Sweep",
            handler="index.handler",
            code=lambda_.Code.from_asset(os.path.join(dirname, './sweeper')),
            runtime=lambda_.Runtime.PYTHON_3_9
        )

        rule.add_target(targets.LambdaFunction(lambdaFn))

ResourceManagerCoreStack(app, "ResourceManager-Shared-Infra",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()