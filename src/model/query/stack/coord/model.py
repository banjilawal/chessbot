# src/model/query/stack/coord/model.py

"""
Module: model.query.stack.coord.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Coord, CoordContext
from model.query import StackQuery


@dataclass
class CoordQuery(StackQuery[Coord]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of coords to search with context.


    Attributes:
        stack: List[Coord]
        context: CoordContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Coord]
    context: CoordContext

