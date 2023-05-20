import os
import subprocess

# import sys

from update_project.utils import get_linux_distribution
from .utils import run_command


def update_apt_packages() -> None:
    print("Updating apt packages...")

    sudo_available = os.system("command -v sudo > /dev/null") == 0

    if sudo_available:
        update_command = ["sudo", "apt", "update"]
        upgrade_command = ["sudo", "apt", "upgrade", "-y"]
    else:
        update_command = ["apt", "update"]
        upgrade_command = ["apt", "upgrade", "-y"]

    run_command(
        update_command,
        success_msg="Apt update completed successfully",
        error_msg="Apt update completed with errors.",
    )

    run_command(
        upgrade_command,
        success_msg="Apt packages updated successfully.",
        error_msg="Apt packages update completed with errors.",
    )


def update_yum_packages() -> None:
    print("Updating YUM packages...")

    sudo_available = os.system("command -v sudo > /dev/null") == 0

    if sudo_available:
        update_command = ["sudo", "yum", "update", "-y"]
    else:
        update_command = ["yum", "update", "-y"]

    run_command(
        update_command,
        success_msg="YUM packages updated successfully.",
        error_msg="YUM packages update completed with errors.",
    )


def update_dnf_packages() -> None:
    print("Updating DNF packages...")
    dnf_update_result = subprocess.run(["sudo", "dnf", "upgrade", "-y"])
    if dnf_update_result.returncode == 0:
        print("DNF packages updated successfully.")
    else:
        print(
            f"DNF packages update completed with errors. Return code: {dnf_update_result.returncode}"
        )


def update_pacman_packages() -> None:
    print("Updating Pacman packages...")
    pacman_update_result = subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
    if pacman_update_result.returncode == 0:
        print("Pacman packages updated successfully.")
    else:
        print(
            f"Pacman packages update completed with errors. Return code: {pacman_update_result.returncode}"
        )


def update_zypper_packages() -> None:
    print("Updating Zypper packages...")
    zypper_update_result = subprocess.run(["sudo", "zypper", "refresh"])
    if zypper_update_result.returncode == 0:
        print("Zypper repositories refreshed successfully.")
    else:
        print(
            f"Zypper repositories refresh completed with errors. Return code: {zypper_update_result.returncode}"
        )

    zypper_upgrade_result = subprocess.run(["sudo", "zypper", "update", "-y"])
    if zypper_upgrade_result.returncode == 0:
        print("Zypper packages updated successfully.")
    else:
        print(
            f"Zypper packages update completed with errors. Return code: {zypper_upgrade_result.returncode}"
        )


def update_app_packages() -> None:
    distro_id = get_linux_distribution()

    if distro_id.lower() in ("ubuntu", "debian"):
        update_apt_packages()
    elif distro_id.lower() in ("fedora"):
        update_dnf_packages()
    elif distro_id.lower() in ("centos", "redhat"):
        update_yum_packages()
    elif distro_id.lower() in ("arch", "manjaro"):
        update_pacman_packages()
    elif distro_id.lower() in ("opensuse", "suse"):
        update_zypper_packages()
    else:
        print(f"Unsupported distribution: {distro_id}. Cannot update packages.")
