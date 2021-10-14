import json
import sys

import numpy as np
from numpy.linalg import norm


def get_dist(flavor=None, requested_vector=None, min_dist=None, requested_instance_name=None):
    selected_flavors = {}
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


def get_shorter_dist(input_available_instances, input_requested_instances, input_preferred_family=None):
    flavors = input_available_instances
    selected_flavors = {}
    for requested_instance_name in input_requested_instances:
        min_dist = sys.maxsize
        requested_instance = input_requested_instances[requested_instance_name]
        requested_vector = np.array([float(requested_instance['mem_size'].split(' ')[0]),
                                     float(requested_instance['num_cores'])])
        for flavor in flavors:
            if not flavor['BareMetal'] and 'ProcessorInfo' in flavor and 'x86_64' in flavor['ProcessorInfo']['SupportedArchitectures']:
                if input_preferred_family and input_preferred_family in flavor['InstanceType']:
                    selected_flavors.update(get_dist(flavor, requested_vector, min_dist, requested_instance_name))
                elif not input_preferred_family:
                    selected_flavors.update(get_dist(flavor, requested_vector, min_dist, requested_instance_name))
    return selected_flavors


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

    instances = {'selected_flavors': get_shorter_dist(available_instances, requested_instances, preferred_family)}
    print(json.dumps(instances))
