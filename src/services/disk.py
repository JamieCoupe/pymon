import psutil

from src.services.utilities import get_size


def get_disk_partitions_and_usage():
    partitions = psutil.disk_partitions()
    disk_partitions = {}
    for partition in partitions:

        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            total_size = partition_usage.total
            used = partition_usage.used
            available = partition_usage.free
            percentage = partition_usage.percent

        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            total_size = 'Permission Error'
            used = 'Permission Error'
            available = 'Permission Error'
            percentage = 'Permission Error'

            continue

        device_info = {"mountpoint": partition.mountpoint, "fs_type": partition.fstype,
                       "usage": {"total": total_size, "used": used, "available": available,
                                 "percentage": f"{percentage}%"}}

        disk_partitions[partition.device] = device_info

    return disk_partitions


def print_disk_partitions_and_usage():
    disk_and_partition_info = get_disk_partitions_and_usage()

    print("=" * 20, "Disk Information", "=" * 20)
    print("=" * 10, "Partitions and Usage", "=" * 10)
    # get all disk partitions
    for device, information in disk_and_partition_info.items():
        print(f"=== Device: {device} ===")
        print(f"  Mountpoint: {information['mountpoint']}")
        print(f"  File system type: {information['fs_type']}")

        print(f"  Total Size: {get_size(information['usage']['total'])}")
        print(f"  Used: {get_size(information['usage']['used'])}")
        print(f"  Free: {get_size(information['usage']['available'])}")
        print(f"  Percentage: {information['usage']['percentage']}%")


def get_disk_io():
    disk_io = psutil.disk_io_counters()
    read = disk_io.read_bytes
    write = disk_io.write_bytes

    return {"read": read, "write": write}


def print_disk_io():
    input_disk_io = get_disk_io()
    print("=" * 10, "IO Since Boot", "=" * 10)
    print(f"   Total read: {get_size(input_disk_io['read'])}")
    print(f"   Total write: {get_size(input_disk_io['write'])}")


if __name__ == '__main__':
    partition_info = get_disk_partitions_and_usage()
    print(partition_info)
    print_disk_partitions_and_usage()
    disk_io_since_boot = get_disk_io()
    print(disk_io_since_boot)
    print_disk_io()
