import psutil

from src.services.utilities import get_size


def get_virtual_memory():
    svmem = psutil.virtual_memory()

    svmem_total = get_size(svmem.total)
    svmem_available = get_size(svmem.available)
    svmem_used = get_size(svmem.used)
    svmem_percentage = svmem.percent

    return_virtual_memory = {'total': svmem_total, 'available': svmem_available, 'used': svmem_used,
                             'percentage': svmem_percentage}

    return return_virtual_memory


def print_virtual_memory():
    virtual_memory = get_virtual_memory()

    print("=" * 20, "Memory Information", "=" * 20)
    print("=" * 10, "Virtual Memory", "=" * 10)
    print(f"Total: {virtual_memory['total']}")
    print(f"Available: {virtual_memory['available']}")
    print(f"Used: {virtual_memory['used']}")
    print(f"Percentage Used: {virtual_memory['percentage']}%")


def get_swap_memory():

    swap = psutil.swap_memory()

    swap_total = get_size(swap.total)
    swap_available = get_size(swap.free)
    swap_used = get_size(swap.used)
    swap_percentage = swap.percent

    return_swap_memory = {'total': swap_total, 'available': swap_available, 'used': swap_used,
                          'percentage': swap_percentage}

    return return_swap_memory


def print_swap_memory():
    swap_memory = get_swap_memory()

    print("=" * 10, "Swap Memory", "=" * 10)
    print(f"Total: {swap_memory['total']}")
    print(f"Available: {swap_memory['available']}")
    print(f"Used: {swap_memory['used']}")
    print(f"Percentage Used: {swap_memory['percentage']}%")


if __name__ == '__main__':
    current_virtual_memory = get_virtual_memory()
    print(current_virtual_memory)
    print_virtual_memory()
    current_swap_memory = get_swap_memory()
    print_swap_memory()
