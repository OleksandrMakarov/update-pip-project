import subprocess
from update_project.utils import get_linux_distribution


def update_apt_packages() -> None:
    print("Updating apt packages...")
    apt_update_result = subprocess.run(["sudo", "apt", "update"])
    if apt_update_result.returncode == 0:
        print("Apt update completed successfully.")
    else:
        print(
            f"Apt update completed with errors. Return code: {apt_update_result.returncode}")

    apt_upgrade_result = subprocess.run(["sudo", "apt", "upgrade", "-y"])
    if apt_upgrade_result.returncode == 0:
        print("Apt packages updated successfully.")
    else:
        print(
            f"Apt packages update completed with errors. Return code: {apt_upgrade_result.returncode}")


def update_yum_packages() -> None:
    print("Updating YUM packages...")
    yum_update_result = subprocess.run(["sudo", "yum", "update", "-y"])
    if yum_update_result.returncode == 0:
        print("YUM packages updated successfully.")
    else:
        print(
            f"YUM packages update completed with errors. Return code: {yum_update_result.returncode}")


def update_dnf_packages() -> None:
    print("Updating DNF packages...")
    dnf_update_result = subprocess.run(["sudo", "dnf", "upgrade", "-y"])
    if dnf_update_result.returncode == 0:
        print("DNF packages updated successfully.")
    else:
        print(
            f"DNF packages update completed with errors. Return code: {dnf_update_result.returncode}")


def update_pacman_packages() -> None:
    print("Updating Pacman packages...")
    pacman_update_result = subprocess.run(
        ["sudo", "pacman", "-Syu", "--noconfirm"])
    if pacman_update_result.returncode == 0:
        print("Pacman packages updated successfully.")
    else:
        print(
            f"Pacman packages update completed with errors. Return code: {pacman_update_result.returncode}")


def update_zypper_packages() -> None:
    print("Updating Zypper packages...")
    zypper_update_result = subprocess.run(["sudo", "zypper", "refresh"])
    if zypper_update_result.returncode == 0:
        print("Zypper repositories refreshed successfully.")
    else:
        print(
            f"Zypper repositories refresh completed with errors. Return code: {zypper_update_result.returncode}")

    zypper_upgrade_result = subprocess.run(["sudo", "zypper", "update", "-y"])
    if zypper_upgrade_result.returncode == 0:
        print("Zypper packages updated successfully.")
    else:
        print(
            f"Zypper packages update completed with errors. Return code: {zypper_upgrade_result.returncode}")


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
        print(
            f"Unsupported distribution: {distro_id}. Cannot update packages.")
