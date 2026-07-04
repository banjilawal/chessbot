# src/model/state/query/stack/coord/model/state.py

"""
Module: model.state.query.stack.coord.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Coord, CoordContext
from model.query import StackQuery
from stack import CoordStackService


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
        stack: CoordStackService
        context: CoordContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: CoordStackService
    context: CoordContext

