import platform
import psutil
from datetime import datetime


def get_sysinfo():

    uname = platform.uname()
    sys_info = {"system": uname.system, "node_name": uname.node, "release": uname.release,
                "version": uname.version, "architecture": uname.machine, "processor": uname.processor}

    return sys_info


def print_sysinfo():
    input_sys_info_dict = get_sysinfo()
    print("=" * 20, "System Information", "=" * 20)
    print("=" * 10, "General", "=" * 10)
    print(f"System: {input_sys_info_dict['system']}")
    print(f"Node Name: {input_sys_info_dict['node_name']}")
    print(f"Release: {input_sys_info_dict['release']}")
    print(f"Version: {input_sys_info_dict['version']}")
    print(f"Machine: {input_sys_info_dict['architecture']}")
    print(f"Processor: {input_sys_info_dict['processor']}")


def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    boot_time = f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

    return boot_time


def print_boot_time():
    boot_time = get_boot_time()
    print("=" * 10, "Boot Time", "=" * 10)
    print(boot_time)


if __name__ == '__main__':
    sys_info_dict = get_sysinfo()
    print_sysinfo()
    print_boot_time()



