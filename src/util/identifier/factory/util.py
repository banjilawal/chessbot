# src/util/identity/factory/util.py

"""
Module: util.identity.factory.util
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Dict
from threading import Lock


class IdFactory:
    _locks: Dict[str, Lock] = {}
    _counters: Dict[str, int] = {}
    _global_lock = Lock()
    
    @classmethod
    def next_id(cls, class_name: str) -> int:
        method = f"{cls.__name__}.next_id"
        
        with cls._global_lock:
            if class_name not in cls._counters:
                cls._counters[class_name] = 0
                cls._locks[class_name] = Lock()
        
        with cls._locks[class_name]:
            cls._counters[class_name] += 1
            return cls._counters[class_name]