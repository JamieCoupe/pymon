def get_size(input_bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    if type(input_bytes) == str:
        return input_bytes
    else:
        for unit in ["", "K", "M", "G", "T", "P"]:
            if input_bytes < factor:
                return f"{input_bytes:.2f}{unit}{suffix}"
            input_bytes /= factor
