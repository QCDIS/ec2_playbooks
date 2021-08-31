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
        
    
    t2_nano = {'MemoryInfo':{'SizeInMiB':'0.5'},'VCpuInfo':{'DefaultVCpus':'1'},'name':'t2.nano'}
    t2_micro = {'MemoryInfo':{'SizeInMiB':'1'},'VCpuInfo':{'DefaultVCpus':'1'},'name':'t2.micro'}
    t2_small = {'MemoryInfo':{'SizeInMiB':'2'},'VCpuInfo':{'DefaultVCpus':'1'},'name':'t2.small'}
    t2_medium = {'MemoryInfo':{'SizeInMiB':'4'},'VCpuInfo':{'DefaultVCpus':'2'},'name':'t2.medium'}
    t2_large = {'MemoryInfo':{'SizeInMiB':'8'},'VCpuInfo':{'DefaultVCpus':'2'},'name':'t2.large'}
    t2_xlarge = {'MemoryInfo':{'SizeInMiB':'16'},'VCpuInfo':{'DefaultVCpus':'4'},'name':'t2.xlarge'}
    t2_2xlarge = {'MemoryInfo':{'SizeInMiB':'32'},'VCpuInfo':{'DefaultVCpus':'8'},'name':'t2.2xlarge'}
    instance_types.append(t2_nano)

    print(json.dumps(instance_types))
