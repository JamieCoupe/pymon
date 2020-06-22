import psutil
from datetime import datetime
import pandas as pd
import time
import os
from random import choice
from src.services.utilities import get_size


def get_random_process():
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            processes.append(process)

    random = choice(processes)

    return random


def get_processes_info():
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

            name = process.name()
            create_time = get_create_time(process)
            number_of_cores = get_number_of_cores(process)
            cpu_usage = get_cpu_usage(process)
            status = process.status()
            nice = get_process_priority(process)
            memory_usage = get_process_memory_usage(process)
            n_threads = get_process_threads(process)

        processes.append({"pid": pid, "name": name, "create_time": create_time, "cores": number_of_cores,
                          "cpu_usage": cpu_usage, "status": status, "nice": nice, "memory_usage": memory_usage,
                          "n_threads": n_threads})

    return processes

# TODO : Add N/A as ouput for permission error. Add into tests as well
def get_process_threads(process):
    try:
        n_threads = process.num_threads()
    except psutil.AccessDenied:
        n_threads = 0

    return n_threads


def get_create_time(process):
    try:
        create_time = datetime.fromtimestamp(process.create_time())
    except OSError:
        create_time = datetime.fromtimestamp(psutil.boot_time())

    return create_time


def get_number_of_cores(process):
    if 'nt' in os.name:
        try:
            # get the number of CPU cores that can execute this process
            cores = len(process.cpu_affinity())
        except psutil.AccessDenied:
            cores = 0
    else:
        cores = 0

    return cores


def get_cpu_usage(process):
    try:
        # get the number of CPU cores that can execute this process
        cpu_usage = process.cpu_percent()
    except psutil.AccessDenied:
        cpu_usage = "N/A"

    return cpu_usage


def get_process_priority(process):
    try:
        # get the process priority (a lower value means a more prioritized process)
        nice = int(process.nice())
    except psutil.AccessDenied:
        nice = 0

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
        username = 0

    return username


if __name__ == '__main__':
    print(f"Random process = {get_random_process()}")
    # process_info = get_processes_info()
    print(get_processes_info())


# https://www.thepythoncode.com/code/make-process-monitor-python