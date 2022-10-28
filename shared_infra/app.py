import os
import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct

app = cdk.App()

class ResourceManagerCoreStack(Stack):
    """ Resource Manager Core Class """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


ResourceManagerCoreStack(app, "ResourceManager-Shared-Infra",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()