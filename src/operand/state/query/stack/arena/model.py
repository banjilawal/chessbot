# src/operand/state/query/stack/arena/operand/state.py

"""
Module: operand.state.query.stack.arena.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Arena, ArenaContext
from operand.query import StackQuery

@dataclass
class ArenaQuery(StackQuery[Arena]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of arenas to search with context.

    Attributes:
        stack: ArenaStackService
        context: ArenaContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: ArenaStackService
    context: ArenaContext

