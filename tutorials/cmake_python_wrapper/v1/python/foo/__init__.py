import ctypes
import numpy as np
import os

__all__ = ['square']

lib = ctypes.cdll.LoadLibrary("libfoo.so")
lib.square.restype = ctypes.c_int
lib.square.argtypes = [ctypes.c_int]


def square(value):
    """
    Parameters
    ----------
    value: int

    Returns
    --------
    value square
    """
    return lib.square(value)

