import os
from typing import Union


def get_or_create_dir(*path_segments: Union[str, os.PathLike]):
    """
    Concats the path segments, creates the directory if it doesn't exist, and returns the directory path.
    """
    dir_path = os.path.join(*path_segments)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path
