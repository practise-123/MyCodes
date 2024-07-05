# Created by        : MyWork
# Created on        : 2024-07-05
import os

from constructs import Construct
from aws_cdk import App, Tags, Stack, Environment
from aws_cdk import aws_ssm

app = App()


# Create stack below #
class MyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        aws_ssm.StringParameter(
            self,
            'topic-name-param',
            parameter_name="/cdk/stack/ssm/param/dummy",
            string_value="dummy"
        )


# ------------------- #
if __name__ == "__main__":
    MyStack(
        app,
        construct_id=f"my-codes-dummy",
        description="dummy stack",
        env=Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))
    )
    tags_dict = {'tier': 'learning', 'application': 'aws-dummy'}
    for key in tags_dict:
        Tags.of(app).add(key, tags_dict.get(key), priority=100)
    app.synth()
