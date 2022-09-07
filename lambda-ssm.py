import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.describe_vpcs()
    # print(response)
    for vpc in client.describe_vpcs()['Vpcs']:
        vpcId = vpc['VpcId']
        vpcName = vpc['Tags'][0]['Value']
        print(vpcId)
        print(vpcName)

        client = boto3.client('ssm')
        response = client.put_parameter(
            Name=vpcName,
            Description='Name of the resource',
            Value=vpcId,
            Type='String',
            Overwrite=True
        )

    client = boto3.client('ec2')
    response = client.describe_subnets()
    # print(response)
    for subnet in client.describe_subnets()['Subnets']:
        subnetId = subnet['SubnetId']
        subnetName = subnet['Tags'][0]['Value']
        print(subnetId)
        print(subnetName)

        client = boto3.client('ssm')    
        response = client.put_parameter(
            Name=subnetName,
            Description='Name of the resource',
            Value=subnetId,
            Type='String',
            Overwrite=True
        )

    client = boto3.client('ec2')
    response = client.describe_route_tables()
    # print(response)
    for routetable in client.describe_route_tables()['RouteTables']:
        routetableId = routetable['RouteTableId']
        routetableName = routetable['Tags'][0]['Value']
        #routetableassociationId = routetable['RouteTableAssociationId']
        print(routetableId)
        print(routetableName)

        client = boto3.client('ssm')
        response = client.put_parameter(
            Name=routetableName,
            Description='Name of your resource',
            Value=routetableId,
            Type='String',
            Overwrite=True
        )

    client = boto3.client('ec2')
    response = client.describe_security_groups()
    # print(response)
    for securitygroup in client.describe_security_groups()['SecurityGroups']:
        securitygroupId = securitygroup['GroupId']
        securitygroupName = securitygroup['Tags'][0]['Value']
        description = securitygroup['Description']
        print(securitygroupId)
        print(securitygroupName)
        print(description)

        client = boto3.client('ssm')
        response = client.put_parameter(
            Name=securitygroupName,
            Description=description,
            Value=securitygroupId,
            Type='String',
            Overwrite=True
        )

    client = boto3.client('ec2')
    response = client.describe_transit_gateway_attachments()
    # print(response)
    for tgwattachments in client.describe_transit_gateway_attachments()['TransitGatewayAttachments']:
        tgwattachmentId = tgwattachments['TransitGatewayAttachmentId']
        tgwattachmentsName = tgwattachments['Tags'][0]['Value']
        print(tgwattachmentId)
        print(tgwattachmentsName)

        client = boto3.client('ssm')
        response = client.put_parameter(
            Name=tgwattachmentsName,
            Description='Name of your resource',
            Value=tgwattachmentId,
            Type='String',
            Overwrite=True
        )

    client = boto3.client('ec2')
    response = client.describe_transit_gateway_route_tables()
    # print(response)
    for tgwroutetable in client.describe_transit_gateway_route_tables()['TransitGatewayRouteTables']:
        tgwroutetableId = tgwroutetable['TransitGatewayRouteTableId']
        tgwroutetableName = tgwroutetable['Tags'][0]['Value']
        print(tgwroutetableId)
        print(tgwroutetableName)

        client = boto3.client('ssm')
        response = client.put_parameter(
            Name=tgwroutetableName,
            Description='Name of your resource',
            Value=tgwroutetableId,
            Type='String',
            Overwrite=True
        )
