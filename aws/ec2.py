import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"], instance.get("PrivateIpAddress"), instance.get("PublicIpAddress"))
