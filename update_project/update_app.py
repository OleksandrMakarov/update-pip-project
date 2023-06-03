import os
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

    sudo_available = os.system("command -v sudo > /dev/null") == 0

    if sudo_available:
        update_command = ["sudo", "dnf", "upgrade", "-y"]
    else:
        update_command = ["dnf", "upgrade", "-y"]

    run_command(
        update_command,
        success_msg="DNF packages updated successfully.",
        error_msg="DNF packages update completed with errors.",
    )


def update_pacman_packages() -> None:
    print("Updating Pacman packages...")

    sudo_available = os.system("command -v sudo > /dev/null") == 0

    if sudo_available:
        update_command = ["sudo", "pacman", "-Syu", "--noconfirm"]
    else:
        update_command = ["pacman", "-Syu", "--noconfirm"]

    run_command(
        update_command,
        success_msg="Pacman packages updated successfully.",
        error_msg="Pacman packages update completed with errors.",
    )


def update_zypper_packages() -> None:
    print("Updating Zypper packages...")

    sudo_available = os.system("command -v sudo > /dev/null") == 0

    if sudo_available:
        refresh_command = ["sudo", "zypper", "refresh"]
        update_command = ["sudo", "zypper", "update", "-y"]
    else:
        refresh_command = ["zypper", "refresh"]
        update_command = ["zypper", "update", "-y"]

    run_command(
        refresh_command,
        success_msg="Zypper repositories refreshed successfully.",
        error_msg="Zypper repositories refresh completed with errors.",
    )

    run_command(
        update_command,
        success_msg="Zypper packages updated successfully.",
        error_msg="Zypper packages update completed with errors.",
    )


def update_app_packages() -> None:
    distro_id = get_linux_distribution().lower()

    if any(name in distro_id for name in ("ubuntu", "debian")):
        update_apt_packages()
    elif any(name in distro_id for name in ("fedora", "centos9")):
        update_dnf_packages()
    elif any(name in distro_id for name in ("centos7", "centos8", "redhat")):
        update_yum_packages()
    elif any(name in distro_id for name in ("arch", "manjaro")):
        update_pacman_packages()
    elif any(name in distro_id for name in ("opensuse", "suse")):
        update_zypper_packages()
    else:
        print(f"Unsupported distribution: {distro_id}. Cannot update packages.")
