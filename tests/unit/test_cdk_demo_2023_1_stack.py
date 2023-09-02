import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_demo_2023_1.cdk_demo_2023_1_stack import CdkDemo20231Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo_2023_1/cdk_demo_2023_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDemo20231Stack(app, "cdk-demo-2023-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
