# src/util/decorator/singleton.py

"""
Module: util.decorator.singleton
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
import threading

__all__ = [
    "singleton"
]


def singleton(cls):
    """A thread-safe decorator for a Singleton."""
    instances = {}  # Dictionary to hold the single instance
    lock = threading.Lock()  # A lock to synchronize threads
    
    def get_instance(*args, **kwargs):
        """Returns the singleton instance of the class."""
        nonlocal instances
        with lock:  # Only one thread can enter this block at a time
            if cls not in instances:  # Check if the instance does not already exist
                instances[cls] = cls(*args, **kwargs)  # Create the singleton instance
        return instances[cls]
    
    return get_instance