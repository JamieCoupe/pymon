import GPUtil


def get_nvidia_gpu_data():
    list_gpus = []
    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append([gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,gpu_total_memory,
                          gpu_temperature, gpu_uuid])

        print(list_gpus)
    return list_gpus


if __name__ == '__main__':
    gpu_data = get_nvidia_gpu_data()
    print(gpu_data)
