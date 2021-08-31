import json
import sys
import boto3

if __name__ == '__main__':
    aws_access_key_id = sys.argv[1]
    aws_secret_access_key = sys.argv[2]
    region = sys.argv[3]
    client = boto3.client(
        'ec2', region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    types = client.describe_instance_types()
    instance_types = []
    for type in types['InstanceTypes']:
        instance_types.append(type)
        
    t2_types = [] 
    t2_nano = {'MemoryInfo':{'SizeInMiB':'0.5'},'VCpuInfo'{'DefaultVCpus':'1'},'name':'t2.nano'}

    print(json.dumps(instance_types))
