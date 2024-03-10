import aws_cdk as core
import aws_cdk.assertions as assertions

from seis616_homework3.seis616_homework3_stack import Seis616Homework3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in seis616_homework3/seis616_homework3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Seis616Homework3Stack(app, "seis616-homework3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
