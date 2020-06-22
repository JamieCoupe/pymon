import psutil
from datetime import datetime
import pandas as pd
import time
import os
from src.services.utilities import get_size


def get_processes_info():
    # the list the contain all process dictionaries
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            print(process)


if __name__ == '__main__':
    # process_info = get_processes_info()
    get_processes_info()


# https://www.thepythoncode.com/code/make-process-monitor-python