# import pytest
import json
from unittest.mock import MagicMock
from update_project.update_pip import update_pip_packages


def test_update_pip_packages(monkeypatch):
    check_output_mock = MagicMock(
        side_effect=[
            b"pip 20.0.1",
            json.dumps([{"name": "package1", "latest_version": "2.0.0"}]).encode(),
        ]
    )
    check_call_mock = MagicMock()
    monkeypatch.setattr(
        "update_project.update_pip.subprocess.check_output", check_output_mock
    )
    monkeypatch.setattr("update_project.update_pip.subprocess.check_call", check_call_mock)

    class MockResponse:
        def __init__(self, url):
            self.data = {"info": {"version": "21.0.1"}}

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def read(self):
            return json.dumps(self.data).encode()

    monkeypatch.setattr(
        "update_project.update_pip.urllib.request.urlopen", lambda url: MockResponse(url)
    )

    update_pip_packages()

    assert check_output_mock.call_count == 2
    assert check_call_mock.call_count == 1
