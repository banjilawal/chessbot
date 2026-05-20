# src/model/query/stack/player/model.py

"""
Module: model.query.stack.player.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Player, PlayerContext
from model.query import StackQuery


@dataclass
class PlayerQuery(StackQuery[Player]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of players to search with context.


    Attributes:
        stack: PlayerStackService
        context: PlayerContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: PlayerStackService
    context: PlayerContext

