# src/domain/interface/archetyped/interface.py

"""
Module: domain.interface.archetyped.interface
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from domain import Archetype


class Archetyped(ABC):
    """
    Role:
        - Interface

    Responsibility:
        1.  Tags an object that has a set of attributes that can identify a unique instance
            in a collection.

    Attributes:

    Provides:
        def archetype(self) -> Archetype

    Super Class:
        Interface
    """
    
    @property
    @abstractmethod
    def archetype(self) -> Archetype:
        pass