#!/usr/bin/env python3
import os


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
        for entry in os.scandir(path):
            if entry.is_file(follow_symlinks=False) and entry.name.endswith(suffix):

                yield entry.path

            elif entry.is_dir(follow_symlinks=False):
                for path in _find_files(suffix, entry.path):
                    yield path

    return list(_find_files(suffix, path))


print(find_files(".c", "./testdir"))
