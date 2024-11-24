"""
This script provides a list of subdirectories in the current directory

"""

import time
import os
from glob import glob
from pathlib import Path


directory = r"venv" # Change venv with your folder
RUNS = 1


def run_os_walk():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [x[0] for x in os.walk(directory)]
    print(f"os.walk\t\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. \tFound dirs: {len(fu)}")


def run_glob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = glob(directory + "/*/")
    print(f"glob.glob\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. \tFound dirs: {len(fu)}")


def run_pathlib_iterdir():
    a = time.time_ns()
    for i in range(RUNS):
        dirname = Path(directory)
        fu = [f for f in dirname.iterdir() if f.is_dir()]
    print(f"pathlib.iterdir\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. \tFound dirs: {len(fu)}")


def run_os_listdir():
    a = time.time_ns()
    for i in range(RUNS):
        dirname = Path(directory)
        fu = [os.path.join(directory, o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory, o))]
    print(f"os.listdir\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. \tFound dirs: {len(fu)}")


def run_os_scandir():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [f.path for f in os.scandir(directory) if f.is_dir()]
    print(f"os.scandir\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms.\tFound dirs: {len(fu)}")


if __name__ == '__main__':
    run_os_scandir()
    run_os_walk()
    run_glob()
    run_pathlib_iterdir()
    run_os_listdir()

