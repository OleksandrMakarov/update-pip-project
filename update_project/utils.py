import os
import distro


def get_linux_distribution():
    return distro.id()


def get_project_version() -> str:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    version_file_path = os.path.join(current_directory, "version")
    with open(version_file_path, "r", encoding="utf-8") as file:
        return file.read().strip()
