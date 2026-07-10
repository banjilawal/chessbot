# src/operand/state/query/stack/game/operand/state.py

"""
Module: operand.state.query.stack.game.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Game
from operand.query import StackQuery


@dataclass
class GameQuery(StackQuery[Game]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

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

