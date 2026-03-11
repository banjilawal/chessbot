# src/logic/span/spanner/category.py

"""
Module: logic.span.spanner.category
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto

class SpannerCategory(Enum):
    PAWN = auto(),
    KNIGHT = auto(),
    BISHOP = auto(),
    ROOK = auto(),
    QUEEN = auto(),
    DIAGONAL = auto(),
    PERPENDICULAR = auto()