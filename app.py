#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import DefaultStackSynthesizer

from cdk_demo_2023_1.cdk_demo_2023_1_stack import CdkDemo20231Stack


app = cdk.App()
CdkDemo20231Stack(app, "CdkDemo20231Stack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='839227026705', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
