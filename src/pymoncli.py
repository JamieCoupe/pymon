from src.services import sysinfo
from src.services import cpu
from src.services import memory
from src.services import disk


def main():

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


if __name__ == '__main__':
    main()
