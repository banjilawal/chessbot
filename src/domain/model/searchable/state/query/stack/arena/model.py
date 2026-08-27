# src/domain/model/state/query/stack/arena/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.arena.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Arena, ArenaContext
from domain.model import StackQuery

@dataclass
class ArenaQuery(StackQuery[Arena]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

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

