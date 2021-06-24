import boto3




def list_available_vm_sizes(compute_client, region = 'eu-west-1', minimum_cores = 1, minimum_memory_MB = 768):
    vm_sizes_list = compute_client.virtual_machine_sizes.list(location=region)
    for vm_size in vm_sizes_list:
        # if vm_size.number_of_cores >= int(minimum_cores) and vm_size.memory_in_mb >= int(minimum_memory_MB):
        print('Name:{0}, Cores:{1}, OSDiskMB:{2}, RSDiskMB:{3}, MemoryMB:{4}, MaxDataDisk:{5}'.format(
            vm_size.name,
            vm_size.number_of_cores,
            vm_size.os_disk_size_in_mb,
            vm_size.resource_disk_size_in_mb,
            vm_size.memory_in_mb,
            vm_size.max_data_disk_count
        ))


if __name__ == '__main__':
    client = boto3.client(
        'ec2','eu-west-1',
    )
    response = client.describe_instances()

    print(response)
    #
    # azure_client_id = sys.argv[1]
    # azure_secret = sys.argv[2]
    # azure_subscription_id = sys.argv[3]
    # azure_tenant = sys.argv[4]
    # region = sys.argv[5]
    # list_available_vm_sizes(client, region = 'EastUS', minimum_cores = 2, minimum_memory_MB = 8192)
