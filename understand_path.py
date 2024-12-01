"""
Directory Listing Script

This script provides a list of subdirectories in the specified directory using various
methods (os.walk, glob, pathlib.iterdir, os.listdir, os.scandir) and measures their performance.

Usage:
    Update the `directory` variable with the desired folder path before running the script.

Methods compared:
    - os.walk
    - glob.glob
    - pathlib.iterdir
    - os.listdir
    - os.scandir
"""

import time
import os
from glob import glob
from pathlib import Path

# Constants
DIRECTORY = "example_directory"  # Change this to your desired folder path
RUNS = 1  # Number of iterations to average timing


def measure_time(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func (function): The function to measure.

    Returns:
        wrapper (function): The wrapped function with timing logic.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time_ns()
        result = func(*args, **kwargs)
        elapsed_time_ms = (time.time_ns() - start_time) / 1_000_000 / RUNS
        print(
            f"{func.__name__}\t\ttook {elapsed_time_ms:.0f} ms.\tFound dirs: {len(result)}")
        return result
    return wrapper


@measure_time
def run_os_walk(directory):
    """
    List subdirectories using os.walk.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of subdirectory paths.
    """
    for _ in range(RUNS):
        subdirs = [x[0] for x in os.walk(directory)]
    return subdirs


@measure_time
def run_glob(directory):
    """
    List subdirectories using glob.glob.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of subdirectory paths.
    """
    for _ in range(RUNS):
        subdirs = glob(f"{directory}/*/")
    return subdirs


@measure_time
def run_pathlib_iterdir(directory):
    """
    List subdirectories using pathlib.Path.iterdir.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of subdirectory paths.
    """
    for _ in range(RUNS):
        subdirs = [f for f in Path(directory).iterdir() if f.is_dir()]
    return subdirs


@measure_time
def run_os_listdir(directory):
    """
    List subdirectories using os.listdir.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of subdirectory paths.
    """
    for _ in range(RUNS):
        subdirs = [
            os.path.join(directory, o)
            for o in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, o))
        ]
    return subdirs


@measure_time
def run_os_scandir(directory):
    """
    List subdirectories using os.scandir.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of subdirectory paths.
    """
    for _ in range(RUNS):
        subdirs = [f.path for f in os.scandir(directory) if f.is_dir()]
    return subdirs


def main():
    """
    Main function to execute all directory listing methods and compare their performance.
    """
    print(f"Listing subdirectories in: {DIRECTORY}\n")
    run_os_scandir(DIRECTORY)
    run_os_walk(DIRECTORY)
    run_glob(DIRECTORY)
    run_pathlib_iterdir(DIRECTORY)
    run_os_listdir(DIRECTORY)


if __name__ == "__main__":
    main()
