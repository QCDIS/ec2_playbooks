import json
import sys

import numpy as np
from numpy.linalg import norm

# if not flavor['BareMetal'] and 'ProcessorInfo' in flavor and 'x86_64' in flavor['ProcessorInfo'][
#     'SupportedArchitectures']:
#     if preferred_family and preferred_family in flavor['InstanceType']:
#         selected_flavors.update(get_dist(flavor, requested_vector, min_dist, requested_instance_name))
#     elif not preferred_family:


def get_shorter_dist(input_available_instances=None, input_requested_instances=None, preferred_family=None):
    flavors = input_available_instances
    the_selected_flavors = {}
    for requested_instance_name in input_requested_instances:
        min_dist = sys.maxsize
        requested_instance = input_requested_instances[requested_instance_name]
        requested_vector = np.array([int(requested_instance['mem_size'].split(' ')[0]),
                                     int(requested_instance['num_cores'])])
        for flavor in flavors:
            if not flavor['BareMetal'] and 'ProcessorInfo' in flavor and 'x86_64' in flavor['ProcessorInfo'][
                'SupportedArchitectures']:
                if preferred_family and preferred_family in flavor['InstanceType']:
                    available_vector = np.array(
                        [int(flavor['MemoryInfo']['SizeInMiB']), int(flavor['VCpuInfo']['DefaultVCpus'])])
                    dist = norm(requested_vector - available_vector)
                    if dist < min_dist:
                        min_dist = dist
                        selected_flavor = {'flavor_name': flavor['InstanceType']}
                        the_selected_flavors[requested_instance_name] = selected_flavor
                elif not preferred_family:
                    available_vector = np.array(
                        [int(flavor['MemoryInfo']['SizeInMiB']), int(flavor['VCpuInfo']['DefaultVCpus'])])
                    dist = norm(requested_vector - available_vector)
                    if dist < min_dist:
                        min_dist = dist
                        selected_flavor = {'flavor_name': flavor['InstanceType']}
                        the_selected_flavors[requested_instance_name] = selected_flavor

    return the_selected_flavors


if __name__ == "__main__":
    available_instances_file_path = sys.argv[1]
    requested_instances_file_path = sys.argv[2]
    preferred_family = None
    if len(sys.argv) == 4:
        preferred_family = sys.argv[3]

    f = open(available_instances_file_path, )
    available_instances = json.load(f)

    f = open(requested_instances_file_path, )
    requested_instances = json.load(f)

    selected_flavors = get_shorter_dist(input_available_instances=available_instances,
                                        input_requested_instances=requested_instances,preferred_family=preferred_family)
    instances = {'selected_flavors': selected_flavors}
    print(json.dumps(instances))
