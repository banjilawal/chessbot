# src/domain/interface/archetyped/__init__.py

"""
Module: domain.interface.archetyped.__init__
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

    Super Class:
    """
    
    @property
    @abstractmethod
    def archetype(self) -> Archetype:
        pass