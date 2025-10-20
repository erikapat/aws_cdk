#!/usr/bin/env python3
import os, aws_cdk as cdk
from lib.stack import FastApiFargateStack
app = cdk.App()
FastApiFargateStack(app, "FastApiFargateStack",
                    env=cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"),
                                        region=os.getenv("CDK_DEFAULT_REGION")))
app.synth()
