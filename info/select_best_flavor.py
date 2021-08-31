import json
import sys

import numpy as np
from numpy.linalg import norm


def get_shorter_dist(available_instances, requested_instances):
    flavors = available_instances
    selected_flavors = {}
    for requested_instance_name in requested_instances:
        min_dist = sys.maxsize
        requested_instance = requested_instances[requested_instance_name]
        requested_vector = np.array([float(requested_instance['mem_size'].split(' ')[0]),
                                     float(requested_instance['num_cores'])])
        # int(requested_instance['disk_size'].split(' ')[0])])

        for flavor in flavors:
            if not flavor['BareMetal'] and 'ProcessorInfo' in flavor and 'x86_64' in flavor['ProcessorInfo']['SupportedArchitectures']:
                available_vector = np.array([float(flavor['MemoryInfo']['SizeInMiB']),
                                             float(flavor['VCpuInfo']['DefaultVCpus'])])
                    # int(requested_instance['disk_size'].split(' ')[0])])
                dist = norm(requested_vector - available_vector)
                if dist < min_dist:
                    min_dist = dist
                    if 'InstanceType' in flavor:
                        selected_flavor = {'flavor_name': flavor['InstanceType']}
                    elif 'name' in flavor:
                        selected_flavor = {'flavor_name': flavor['name']}
                    selected_flavors[requested_instance_name] = selected_flavor

    return selected_flavors


if __name__ == "__main__":
    available_instances_file_path = sys.argv[1]
    requested_instances_file_path = sys.argv[2]

    f = open(available_instances_file_path, )
    available_instances = json.load(f)

    f = open(requested_instances_file_path, )
    requested_instances = json.load(f)

    selected_flavors = get_shorter_dist(available_instances, requested_instances)
    instances = {'selected_flavors': selected_flavors}
    print(json.dumps(instances))
