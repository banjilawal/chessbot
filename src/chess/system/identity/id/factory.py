# src/chess/system/identity/id/factory.py

"""
Module: chess.system.identity.id.factory
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from typing import Dict
from threading import Lock

class IdFactory:
    _locks: Dict[str, Lock] = {}
    _counters: Dict[str, int] = {}
    _global_lock = Lock()
    
    @classmethod
    def next_id(cls, class_name: str) -> int:
        method = "IDFactory.next_id"
        
        with cls._global_lock:
            if class_name not in cls._counters:
                cls._counters[class_name] = 0
                cls._locks[class_name] = Lock()
                
        with cls._locks[class_name]:
            cls._counters[class_name] += 1
            return cls._counters[class_name]