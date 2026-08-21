# src/dossier/model/state/query/stack/coord/dossier/model/state.py

"""
Module: domain.model.state.query.stack.coord.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Coord, CoordContext
from domain.model import StackQuery
from collection.stack import CoordStackService


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

