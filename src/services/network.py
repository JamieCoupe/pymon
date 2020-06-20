import psutil
import socket
from src.services.utilities import get_size


def get_network_interfaces():
    if_addrs = psutil.net_if_addrs()

    network_interfaces = {"af_inet": [], "af_packet": []}

    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                ip_address = address.address
                netmask = address.netmask
                ip_broadcast = address.broadcast
                result = {"ip_address": ip_address, "net_mask": netmask, "ip_broadcast": ip_broadcast}
                network_interfaces["af_inet"].append(result)

            elif str(address.family) == 'AddressFamily.AF_PACKET':
                mac_address = address.address
                netmask = address.netmask
                mac_broadcast = address.broadcast
                result = {"ip_address": mac_address, "net_mask": netmask, "ip_broadcast": mac_broadcast}
                network_interfaces["af_packet"].append(result)

    return network_interfaces


def print_network_interfaces():
    network_interface_data = get_network_interfaces()

    print("=" * 20, "Network", "=" * 20)
    print("=" * 10, "Interfaces", "=" * 10)

    print("=== AF_INET ===")
    if not network_interface_data["af_inet"]:
        print("No Interfaces")
    else:
        for interface in network_interface_data["af_inet"]:
            print(f"    Interface : {(network_interface_data['af_inet'].index(interface) + 1)}")
            print(f"    IP Address = {interface['ip_address']}")
            print(f"    NET Mask = {interface['net_mask']}")
            print(f"    IP Broadcast = {interface['ip_broadcast']}\n")

    print("=== AF_PACKET ===")
    if not network_interface_data["af_packet"]:
        print("No Interfaces")
    else:
        for interface in network_interface_data["af_inet"]:
            print(f"    MAC Address = {interface['mac_address']}")
            print(f"    NET Mask = {interface['net_mask']}")
            print(f"    MAC Broadcast = {interface['mac_broadcast']}")


def get_network_io():
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent
    received = net_io.bytes_recv

    return {"sent": sent, "received": received}


def print_network_io():
    input_network_io = get_network_io()

    print("=" * 10, "Network IO", "=" * 10)
    print(f"Total sent: {get_size(input_network_io['sent'])}")
    print(f"Total received: {get_size(input_network_io['received'])}")


if __name__ == '__main__':
    network_interface_results = get_network_interfaces()
    print(network_interface_results)
    print_network_interfaces()
    network_io = get_network_io()
    print(network_io)
    print_network_io()
