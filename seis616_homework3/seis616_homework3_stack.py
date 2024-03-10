# Chinh Pham
# SEIS616 
# Based off of CDK_lab_web_server_stack.py

import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_deployment as s3deployment

from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)

from constructs import Construct

class Seis616Homework3Stack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
