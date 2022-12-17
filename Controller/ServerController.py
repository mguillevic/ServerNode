import subprocess
import psutil

def recup_server_props():
    cpu_usage = psutil.cpu_percent(0.1)
    available_ram = psutil.virtual_memory().available
    return {
        'cpu_usage':cpu_usage,
        'available_ram': available_ram,
    }


def run_shell(name):
    command = ['sudo',"bash","../shell_scripts/lancement_jeu.sh",name]
    result = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return result
