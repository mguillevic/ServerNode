import psutil

def recup_server_props():
    cpu_usage = psutil.cpu_percent(0.1)
    available_ram = psutil.virtual_memory().available
    return {
        'cpu_usage':cpu_usage,
        'available_ram': available_ram,
    }