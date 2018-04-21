import os
import subprocess
import functools


def shell_error_handler(func):
    """shell error headler"""
    @functools.wraps(func)
    def wrapper(*args, **kw):
        """wrapper"""
        output = func(*args, **kw).communicate()
        if output[1]:
            print(output[1])
    return wrapper


@shell_error_handler
def my_shell(args=None):
    """shell wrapper"""
    return subprocess.Popen(args, stdout=subprocess.PIPE)


def embeded_shell(args):
    """shell wrapper"""
    return subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
