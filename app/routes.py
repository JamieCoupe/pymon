from app import app
from flask import render_template

from pymoncore.services import sysinfo
from pymoncore.services import cpu
from pymoncore.services import memory
from pymoncore.services import disk
from pymoncore.services import network
from pymoncore.services import process
from pymoncore.services.utilities import get_size


@app.route('/')
@app.route('/index')
def get_index():

    # Sysinfo
    static_sysinfo = sysinfo.get_sysinfo()
    boot_time = sysinfo.get_boot_time()

    # CPU
    cpu_static = cpu.get_static_info()
    cpu_frequency = cpu.get_current_frequency()
    cpu_usage_total = cpu.get_total_cpu_usage()
    cpu_usage_cores = cpu.get_usage_per_core()

    # Memory
    virtual_memory = memory.get_virtual_memory()
    swap_memory = memory.get_swap_memory()

    # Disk
    disk_partition_info = disk.get_disk_partitions_and_usage()
    disk_io = disk.get_disk_io()

    # Network
    network_interfaces = network.get_network_interfaces()
    network_io = network.get_network_io()

    # Processes
    running_processes = process.get_all_processes_info()
    columns = "name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores"
    process_df = process.construct_dataframe(running_processes, "memory_usage", columns, False)

    return render_template("index.html", sysinfo=static_sysinfo, boottime=boot_time, cpu_static=cpu_static,
                           cpu_freq=cpu_frequency, cpu_usage_total=cpu_usage_total, cpu_usage_cores=cpu_usage_cores,
                           virtual_memory=virtual_memory, swap_memory=swap_memory,
                           disk_partitions=disk_partition_info, disk_io=disk_io,
                           network_interfaces=network_interfaces, network_io=network_io,
                           processes=process_df.to_string())


@app.route('/home')
def get_home():
    static_sysinfo = sysinfo.get_sysinfo()
    disk_io = disk.get_disk_io()
    net_io = network.get_network_io()
    total_cpu_usage = cpu.get_total_cpu_usage()
    total_memory_usage = memory.get_virtual_memory()
    return render_template("home.html", os_type=static_sysinfo['system'], hostname=static_sysinfo['node_name'],
                           release=static_sysinfo['release'],
                           cpu_usage=total_cpu_usage,
                           memory_usage=total_memory_usage['percentage'],
                           disk_read=get_size(disk_io['read']), disk_write=get_size(disk_io['write']),
                           net_sent=get_size(net_io['sent']), net_received=get_size(net_io['received']))


@app.route('/test')
def get_test():
    return render_template("test.html")
