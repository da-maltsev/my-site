import os

local_path = os.path.dirname(os.path.dirname(__file__))


def setup_path(file_path: str) -> str:
    return os.path.join(local_path, file_path)


__all__ = ["setup_path"]
