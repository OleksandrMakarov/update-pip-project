import pytest
import json
from unittest.mock import MagicMock
from update_project.update_packages import (
    get_linux_distribution,
    update_pip_packages,
    update_apt_packages,
    update_yum_packages,
    update_dnf_packages,
    update_pacman_packages,
    update_zypper_packages,
    update_app_packages,
)


def test_get_linux_distribution(monkeypatch):
    monkeypatch.setattr("update_project.update_packages.distro.id", lambda: "ubuntu")
    assert get_linux_distribution() == "ubuntu"


def test_update_pip_packages(monkeypatch):
    check_output_mock = MagicMock(
        side_effect=[
            b"pip 21.0.1",
            json.dumps([{"name": "package1", "latest_version": "2.0.0"}]).encode(),
        ]
    )
    check_call_mock = MagicMock()
    monkeypatch.setattr("update_project.update_packages.subprocess.check_output", check_output_mock)
    monkeypatch.setattr("update_project.update_packages.subprocess.check_call", check_call_mock)

    class MockResponse:
        def __init__(self, url):
            self.data = {"info": {"version": "21.0.1"}}

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def read(self):
            return json.dumps(self.data).encode()

    monkeypatch.setattr("update_project.update_packages.urllib.request.urlopen", lambda url: MockResponse(url))

    update_pip_packages()

    assert check_output_mock.call_count == 2
    assert check_call_mock.call_count == 1



@pytest.mark.parametrize(
    "distro_id, update_func",
    [
        ("ubuntu", update_apt_packages),
        ("debian", update_apt_packages),
        ("fedora", update_dnf_packages),
        ("centos", update_yum_packages),
        ("redhat", update_yum_packages),
        ("arch", update_pacman_packages),
        ("manjaro", update_pacman_packages),
        ("opensuse", update_zypper_packages),
        ("suse", update_zypper_packages),
    ],
)
def test_update_app_packages(monkeypatch, distro_id, update_func):
    monkeypatch.setattr("update_project.update_packages.get_linux_distribution", lambda: distro_id)
    update_func_mock = MagicMock()
    monkeypatch.setattr("update_project.update_packages." + update_func.__name__, update_func_mock)

    update_app_packages()

    update_func_mock.assert_called_once()


def test_update_app_packages_unsupported(monkeypatch, capsys):
    monkeypatch.setattr("update_project.update_packages.get_linux_distribution", lambda: "unsupported")

    update_app_packages()

    captured = capsys.readouterr()
    assert "Unsupported distribution: unsupported. Cannot update packages." in captured.out
