import argparse
import os
import time
from src.services import sysinfo
from src.services import cpu
from src.services import memory
from src.services import disk
from src.services import network
from src.services import process
from src.services import utilities


def print_full_sysinfo():
    # General information
    sysinfo.print_sysinfo()
    sysinfo.print_boot_time()
    # CPU information
    cpu.print_static_info()
    cpu.print_dynamic_info()
    # Memory information
    memory.print_virtual_memory()
    memory.print_swap_memory()
    # Disk Information
    disk.print_disk_partitions_and_usage()
    disk.print_disk_io()
    # Network Information
    network.print_network_interfaces()
    network.print_network_io()


def print_processes(columns, descending, df, live_update, n, sort_by):
    if n == 0:
        print(df.to_string())
    elif n > 0:
        print(df.head(n).to_string())
    # print continuously
    while live_update:
        # get all process info
        processes = process.get_all_processes_info()
        df = process.construct_dataframe(processes, sort_by, columns, descending)
        # clear the screen depending on your OS
        os.system("cls") if "nt" in os.name else os.system("clear")
        if n == 0:
            print(df.to_string())
        elif n > 0:
            print(df.head(n).to_string())
        time.sleep(0.7)


def main():

    # Process Header
    print("=" * 20, "Processes", "=" * 20)

    parser = argparse.ArgumentParser(description="Process Viewer & Monitor")
    parser.add_argument("-c", "--columns", help="""Columns to show,
                                                available are name,create_time,cores,cpu_usage,status,nice,memory_usage,
                                                read_bytes,write_bytes,n_threads,username.
                                                Default is name,cpu_usage,memory_usage,read_bytes,write_bytes,status,
                                                create_time,nice,n_threads,cores.""",
                        default="name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,"
                                "cores")
    parser.add_argument("-s", "--sort-by", dest="sort_by", help="Column to sort by, default is memory_usage .",
                        default="memory_usage")
    parser.add_argument("--descending", "-d", action="store_true", help="Whether to sort in descending order.")
    parser.add_argument("-n", help="Number of processes to show, will show all if 0 is specified, default is 25 .",
                        default=25)
    parser.add_argument("-u", "--live-update", action="store_true", help="Whether to keep the program on and updating "
                                                                         "process information each second")
    parser.add_argument("-p", "--processes", dest="process", action="store_true", help="Only show processes")
    parser.add_argument("-si", "--sysinfo", dest="sysinfo", action="store_true", help="Only show sysinfo")

    # parse arguments
    args = parser.parse_args()
    columns = args.columns
    sort_by = args.sort_by
    descending = args.descending
    process_only = args.process
    sysinfo_only = args.sysinfo
    n = int(args.n)

    live_update = args.live_update
    # print the processes for the first time
    processes = process.get_all_processes_info()
    df = process.construct_dataframe(processes, sort_by, columns, descending)

    if process_only:
        print_processes(columns, descending, df, live_update, n, sort_by)

    elif sysinfo_only:
        print_full_sysinfo()
    else:
        print_full_sysinfo()
        print_processes(columns, descending, df, live_update, n, sort_by)


if __name__ == '__main__':
    main()
