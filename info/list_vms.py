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
        
    
    t2_nano = {'MemoryInfo':{'SizeInMiB':'500'},'VCpuInfo':{'DefaultVCpus':'1'},'InstanceType':'t2.nano','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_micro = {'MemoryInfo':{'SizeInMiB':'1000'},'VCpuInfo':{'DefaultVCpus':'1'},'InstanceType':'t2.micro','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_small = {'MemoryInfo':{'SizeInMiB':'2000'},'VCpuInfo':{'DefaultVCpus':'1'},'InstanceType':'t2.small','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_medium = {'MemoryInfo':{'SizeInMiB':'4000'},'VCpuInfo':{'DefaultVCpus':'2'},'InstanceType':'t2.medium','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_large = {'MemoryInfo':{'SizeInMiB':'8000'},'VCpuInfo':{'DefaultVCpus':'2'},'InstanceType':'t2.large','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_xlarge = {'MemoryInfo':{'SizeInMiB':'16000'},'VCpuInfo':{'DefaultVCpus':'4'},'InstanceType':'t2.xlarge','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    t2_2xlarge = {'MemoryInfo':{'SizeInMiB':'32000'},'VCpuInfo':{'DefaultVCpus':'8'},'InstanceType':'t2.2xlarge','BareMetal':False,'ProcessorInfo':{'SupportedArchitectures':'x86_64'}}
    instance_types.append(t2_nano)
    instance_types.append(t2_micro)
    instance_types.append(t2_small)
    instance_types.append(t2_medium)
    instance_types.append(t2_large)
    instance_types.append(t2_xlarge)
    instance_types.append(t2_2xlarge)

    print(json.dumps(instance_types))
