import psutil
from datetime import datetime
import pandas as pd
import os
from random import choice
from pymoncore.services.utilities import get_size


def get_random_process():
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            processes.append(process)

    random = choice(processes)

    return random


def get_all_processes_info():
    # the list the contain all process dictionaries
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            pid = process.pid
            if pid == 0:
                # System Idle Process for Windows NT, useless to see
                continue

            name = get_process_name(process)
            create_time = get_process_create_time(process)
            number_of_cores = get_process_core_usage(process)
            cpu_usage = get_process_cpu_usage(process)
            status = get_process_cpu_usage(process)
            nice = get_process_priority(process)
            memory_usage = get_process_memory_usage(process)
            n_threads = get_process_threads(process)
            process_io = get_process_io(process)

        processes.append({"pid": pid, "name": name, "create_time": create_time, "cores": number_of_cores,
                          "cpu_usage": cpu_usage, "status": status, "nice": nice, "memory_usage": memory_usage,
                          "n_threads": n_threads, "read_bytes": process_io["read_bytes"],
                          "write_bytes": process_io["write_bytes"]})

    return processes


def get_process_name(process):
    try:
        name = process.name()
    except psutil.AccessDenied:
        name = "N/A"

    return name


def get_process_threads(process):
    try:
        n_threads = process.num_threads()
    except psutil.AccessDenied:
        n_threads = "AccessDenied"

    return n_threads


def get_process_create_time(process):
    try:
        create_time = datetime.fromtimestamp(process.create_time())
    except OSError:
        create_time = datetime.fromtimestamp(psutil.boot_time())

    return create_time


def get_process_core_usage(process):
    if 'nt' in os.name:
        try:
            # get the number of CPU cores that can execute this process
            cores = len(process.cpu_affinity())
        except psutil.AccessDenied:
            cores = "AccessDenied"
    else:
        cores = "Not On Platform"

    return cores


def get_process_cpu_usage(process):
    try:
        # get the number of CPU cores that can execute this process
        cpu_usage = process.cpu_percent()
    except psutil.AccessDenied:
        cpu_usage = "AccessDenied"

    return cpu_usage


def get_process_status(process):
    try:
        status = process.status()
    except psutil.AccessDenied:
        status = "AccessDenied"

    return status


def get_process_priority(process):
    try:
        # get the process priority (a lower value means a more prioritized process)
        nice = int(process.nice())
    except psutil.AccessDenied:
        nice = "AccessDenied"

    return nice


def get_process_memory_usage(process):
    try:
        # get the memory usage in bytes
        memory_usage = process.memory_full_info().uss
    except psutil.AccessDenied:
        memory_usage = 0

    return memory_usage


def get_process_io(process):
    # total process read and written bytes
    try:
        io_counters = process.io_counters
        read_bytes = io_counters.read_bytes
        write_bytes = io_counters.write_bytes

    except AttributeError:
        read_bytes = "N/A"
        write_bytes = "N/A"

    process_io = {"read_bytes": read_bytes, "write_bytes": write_bytes}

    return process_io


def get_process_username(process):
    try:
        username = process.username()
    except psutil.AccessDenied:
        username = "AccessDenied"

    return username


def construct_dataframe(process_dict, sort_column, columns_to_show, descending):
    df = pd.DataFrame(process_dict)
    df.set_index('pid', inplace=True)
    df.sort_values(sort_column, inplace=True, ascending=not descending)
    # pretty printing bytes
    df['memory_usage'] = df['memory_usage'].apply(get_size) if type(df['memory_usage']) is int else df['memory_usage']
    df['write_bytes'] = df['write_bytes'].apply(get_size) if type(df['write_bytes']) is int else df['write_bytes']
    df['read_bytes'] = df['read_bytes'].apply(get_size) if type(df['read_bytes']) is int else df['read_bytes']
    # convert to proper date format
    df['create_time'] = df['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
    # reorder and define used columns
    df = df[columns_to_show.split(",")]
    return df


if __name__ == '__main__':
    print(f"Random process = {get_random_process()}")
    all_processes = get_all_processes_info()
    print(all_processes)
    print(construct_dataframe(all_processes, "memory_usage", "name,cpu_usage,memory_usage,read_bytes,write_bytes,"
                                                             "status,create_time,nice,n_threads,cores").to_string())


# https://www.thepythoncode.com/code/make-process-monitor-python