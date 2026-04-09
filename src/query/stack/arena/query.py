# src/query/stack/arena/query.py

"""
Module: query.stack.arena.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Arena
from query import StackQuery
from search import ArenaContext


@dataclass
class ArenaQuery(StackQuery[Arena]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

    Responsibilities:
        1.  A list of arenas to search with context.


    Attributes:
        stack: List[Arena]
        context: ArenaContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Arena]
    context: ArenaContext

