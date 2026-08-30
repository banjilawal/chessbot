# src/domain/search/model/square/category.py

"""
Module: domain.search.model.square.category
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class SquareType(Enum):
    SQUARE = auto(),
    HOME_SQUARE = auto(),