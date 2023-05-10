# import pytest
# import json
# from unittest.mock import MagicMock
# from update_project.main import (
#     get_linux_distribution,
#     update_pip_packages,
#     update_apt_packages,
#     update_yum_packages,
#     update_dnf_packages,
#     update_pacman_packages,
#     update_zypper_packages,
#     update_app_packages,
#     get_version_from_pyproject_toml
# )


# def test_get_linux_distribution(monkeypatch):
#     monkeypatch.setattr(
#         "update_project.main.distro.id", lambda: "ubuntu")
#     assert get_linux_distribution() == "ubuntu"


# @pytest.mark.parametrize(
#     "distro_id, update_func",
#     [
#         ("ubuntu", update_apt_packages),
#         ("debian", update_apt_packages),
#         ("fedora", update_dnf_packages),
#         ("centos", update_yum_packages),
#         ("redhat", update_yum_packages),
#         ("arch", update_pacman_packages),
#         ("manjaro", update_pacman_packages),
#         ("opensuse", update_zypper_packages),
#         ("suse", update_zypper_packages),
#     ],
# )
# def test_update_app_packages(monkeypatch, distro_id, update_func):
#     monkeypatch.setattr(
#         "update_project.main.get_linux_distribution", lambda: distro_id)
#     update_func_mock = MagicMock()
#     monkeypatch.setattr("update_project.main." +
#                         update_func.__name__, update_func_mock)

#     update_app_packages()

#     update_func_mock.assert_called_once()


# def test_update_app_packages_unsupported(monkeypatch, capsys):
#     monkeypatch.setattr(
#         "update_project.main.get_linux_distribution", lambda: "unsupported")

#     update_app_packages()

#     captured = capsys.readouterr()
#     assert "Unsupported distribution: unsupported. Cannot update packages." in captured.out


# def test_get_version_from_pyproject_toml():
#     result = get_version_from_pyproject_toml()
#     assert type(result) is str
#     assert len(result) >= 5
