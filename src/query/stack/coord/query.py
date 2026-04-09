# src/query/stack/coord/query.py

"""
Module: query.stack.coord.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Coord, CoordContext
from query import StackQuery


@dataclass
class CoordStackQuery(StackQuery[Coord]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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

