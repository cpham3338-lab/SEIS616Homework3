from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkLabWebServerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        cdk_lab_vpc = ec2.Vpc(self, "cdk_lab_vpc", 
                              ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
                              subnet_configuration=[ec2.SubnetConfiguration(name="PublicSubnet01", subnet_type=ec2.SubnetType.PUBLIC)]
                              )
                              
        InstanceRole = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        InstanceRole.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))
        
        cdk_lab_web_instance1 = ec2.instance(self, "cdk_lab_web_instance1", 
                                             vpc=cdk_lab_vpc, 
                                             instance_type=ec2.InstanceType("t2.micro"),
                                             machine_image=ec2.AmazoneLinuxImage(genereation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                             role=InstanceRole
                                             )
                                             
        