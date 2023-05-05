import subprocess
import distro


def get_linux_distribution():
    return distro.id()


def run_command(args, success_msg, error_msg):
    result = subprocess.run(args, check=False, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{success_msg}\n")
    else:
        print(f"{error_msg} Return code: {result.stderr}")
