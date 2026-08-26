# src/domain/search/search.py

"""
Module: domain.search.search
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Collectable


class Searchable(Collectable, ABC):
    """
    Role:
        - Interface

    Responsibility:
        1.  Allows a Collectable to have a SearchContext.

    Attributes:

    Provides:

    Super Class:
    """
    pass