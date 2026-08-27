# src/domain/model/searchable/state/query/stack/game/dossier/model/searchable/state.py

"""
Module: domain.model.searchable.state.query.stack.game.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model import Game
from domain.model import StackQuery


@dataclass
class GameQuery(StackQuery[Game]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

    Responsibilities:
        1.  A list of games to search with context.


    Attributes:
        stack: List[Game]
        context: GameContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Game]
    context: GameContext

