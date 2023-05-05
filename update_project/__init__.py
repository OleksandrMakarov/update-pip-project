import importlib.metadata

try:
    __version__ = importlib.metadata.version("update-pip-packages")
except importlib.metadata.PackageNotFoundError:
    # The package is not installed, you may be in development mode.
    __version__ = "0.0.0"