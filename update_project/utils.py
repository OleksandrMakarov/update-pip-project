import subprocess
import distro

def get_linux_distribution():
    return distro.id()


def run_command(args):
    return subprocess.run(
        args,
        check=False,
        capture_output=True,
        text=True
    )
