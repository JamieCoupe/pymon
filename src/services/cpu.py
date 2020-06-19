import psutil


def get_static_info():
    # Cores physical/logical
    physical_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)

    # Frequencies
    cpufreq = psutil.cpu_freq()
    max_frequency = f"{cpufreq.max:.2f}"
    min_frequency = f"{cpufreq.min:.2f}"

    static_cpu = {"physical_cores" : physical_cores, "total_cores": total_cores, "max_frequency": max_frequency,
                  "min_frequency": min_frequency}

    return static_cpu


def print_static_info():
    input_static_cpu_info = get_static_info()
    print("=" * 20, "CPU Info", "=" * 20)
    print("Physical cores:", input_static_cpu_info['physical_cores'])
    print("Total cores:", input_static_cpu_info['total_cores'])

    print(f"Max Frequency: {input_static_cpu_info['max_frequency']}Mhz")
    print(f"Min Frequency: {input_static_cpu_info['min_frequency']}Mhz")


def get_current_frequency():
    # Returns cpu frequency in Mhz
    return psutil.cpu_freq().current


def get_usage_per_core():
    cpu_usage = list()

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        # if returns 0.0 probably an error in the count. Retry upto 3 times.

        retry_counter = 0

        if percentage == 0.0 and retry_counter < 3:
            i = i - 1
            retry_counter = retry_counter + 1
            continue

        elif retry_counter > 2:
            break

        else:
            cpu_usage.append(percentage)

    return cpu_usage


def get_total_cpu_usage():
    return psutil.cpu_percent(interval=1)


def print_dynamic_info():
    current_frequency = get_current_frequency()
    usage_per_core = get_usage_per_core()
    total_cpu_usage = get_total_cpu_usage()

    print(f"Current Frequency: {current_frequency}Mhz")

    for usage in usage_per_core:
        core_number = usage_per_core.index(usage) + 1
        print(f"Core {core_number}: {usage}%")

    print(f"Total CPU Usage avg: {total_cpu_usage}%")


if __name__ == '__main__':
    static_info = get_static_info()
    print_static_info(static_info)
    print_dynamic_info()

