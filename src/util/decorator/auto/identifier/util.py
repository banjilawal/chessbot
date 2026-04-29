# src/util/decorator/auto/identifier/util.py

"""
Module: util.decorator.auto.identifier.util
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from itertools import count
from threading import Lock
from typing import Type, TypeVar

T = TypeVar("T")

__all__ = [
    # ======================# AUTO_ID #======================#
    "auto_id",
]
# ======================# AUTO_ID #======================#

def auto_id(cls: Type[T]) -> Type[T]:
    """
    Decorator that adds automatic ID generation to team_name class.
    Each decorated class gets its own independent ID counter starting at 1.
    Thread-safe.
    """
    cls._id_counter = count(1)
    cls._id_lock = Lock()
    
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        with cls._id_lock:
            self._visitor_id = next(cls._id_counter)
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    cls.id = property(lambda self: self._visitor_id)
    
    return cls