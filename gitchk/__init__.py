from importlib.metadata import version


def get_version() -> str:
    return version("gitchk")


__version__ = get_version()
