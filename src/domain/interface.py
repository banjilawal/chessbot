# src/domain/interface.py

"""
Module: domain.interface
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC


class Collectable(ABC):
    """
    Role:
        - Interface

    Responsibility:
        1.  Tags a DomainObject that can be in a collection.
        2.  Collectable DomainObject is searchable.

    Attributes:

    Provides:

    Super Class:
    """
    pass