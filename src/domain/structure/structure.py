# src/domain/structures/structure.py

"""
Module: domain.structures.structure
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Collectable


class StructuralWrapper(Collectable, ABC):
    """
    Role:
        -   Structural Wrapper

    Responsibility:
        1.  Wraps DataModelObject giving it additional features.

    Attributes:

    Provides:

    Super Class:
    """
    pass