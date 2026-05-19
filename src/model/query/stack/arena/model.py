# src/model/query/stack/arena/model.py

"""
Module: model.query.stack.arena.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Arena, ArenaContext
from model.query import StackQuery

@dataclass
class ArenaQuery(StackQuery[Arena]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of arenas to search with context.

    Attributes:
        items: List[Arena]
        context: ArenaContext

    Provides:

    Super Class:
        StackQuery
    """
    items: List[Arena]
    context: ArenaContext

