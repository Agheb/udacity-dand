#!/usr/bin/env python3
import os
import errno


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
        """
        A generator function to find files with file name suffix"

        Args:
          suffix(str): suffix if the file name to be found
          path(str): path of the file system
        """

        try:
            for entry in os.scandir(path):
                if entry.is_file(follow_symlinks=False) and entry.name.endswith(suffix):

                    yield entry.path

                elif entry.is_dir(follow_symlinks=False):
                    for path in _find_files(suffix, entry.path):
                        yield path

        except OSError as error:
            if error.errno == errno.ENOENT:
                print("No such directory found")
            else:
                raise

    return list(_find_files(suffix, path))


print(find_files(".c", "./testdir"))
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(".h", "./testdir"))
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']

print(find_files(".py", "./testdir"))
# []

print(find_files("n", ""))
# No such directory
# []

print(find_files("notgood", "./testdir"))
# []
