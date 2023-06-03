import subprocess
import distro


def get_linux_distribution():
    return f"{distro.id()}{distro.version()}"


def run_command(args, success_msg, error_msg, stdout=True):
    result = subprocess.run(args, check=False, capture_output=True, text=True)
    if stdout:
        print(f"{result.stdout}\n")
    if result.returncode == 0:
        print(f"{success_msg}\n")
    else:
        print(f"{error_msg} Return code: {result.stderr}")
