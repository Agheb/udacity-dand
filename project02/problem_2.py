#!/usr/bin/env python3

from os import listdir
from os.path import isfile, isdir, join


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    def _find_files(suffix, path):
        for l in listdir(path):
            new_path = join(path, l)
            if isfile(new_path) and new_path.endswith(suffix):
                yield new_path
            elif isdir(new_path):
                for item in _find_files(suffix, new_path):
                    yield item

    return list(_find_files(suffix, path))


print(find_files(".c", "./testdir"))
