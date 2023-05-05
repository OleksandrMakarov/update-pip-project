import sys
import json
import urllib.request
import subprocess
from .utils import run_command


def update_pip_packages() -> None:
    print("Checking for pip updates...")

    pip_version = (
        subprocess.check_output([sys.executable, "-m", "pip", "--version"])
        .decode()
        .split()[1]
    )

    with urllib.request.urlopen("https://pypi.org/pypi/pip/json") as response:
        pip_latest_version = json.load(response)["info"]["version"]

    if pip_version != pip_latest_version:
        print(
            f"Updating pip from version {pip_version} to version {pip_latest_version}..."
        )
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
        )
        print("Pip updated successfully.")
    else:
        print(f"Pip is already up-to-date (version {pip_version}).")

    print("Checking for available pip package updates...")
    outdated_packages = subprocess.check_output(
        [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"]
    ).decode()
    packages_to_update = [pkg["name"] for pkg in json.loads(outdated_packages)]

    if not packages_to_update:
        print("All pip packages are up-to-date.")
    else:
        print("Updating pip packages...")
        for package in packages_to_update:
            run_command(
                [sys.executable, "-m", "pip", "install", "--upgrade", package],
                success_msg=f"{package} updated successfully.",
                error_msg=f"Error updating {package}.",
            )
        print("Pip packages update completed.")
