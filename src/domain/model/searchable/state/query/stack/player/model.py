# src/domain/model/state/query/stack/player/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.player.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Player, PlayerContext
from domain.model import StackQuery


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

