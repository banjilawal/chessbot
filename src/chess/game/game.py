# src/chess/game/game.py

"""
Module: chess.game.game
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List, Optional

from chess.agent import Agent
from chess.game.result import GameUpdate


class Game:
    """
    # ROLE: Controller

    # RESPONSIBILITIES:
    Interface players use to change the Arena's state.

    # PARENT
    None

    # PROVIDES:
    Game

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (Agent)
        *   black_player (Agent)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _arena: Arena
    _white_player: Agent
    _black_player: Agent
    _timeline: GameResultStack
    
    def __init__(self, id: int, white_player: Agent, black_player: Agent, arena: Arena):
        self._id = id
        self._arena = arena
        self._white_player = white_player
        self._black_player = black_player
        self._timeline = GameResultStack()
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def white_player(self) -> Agent:
        return self._white_player
    
    @property
    def black_player(self) -> Agent:
        return self._black_player
    
    @property
    def players(self) -> List[Agent]:
        return [self._white_player, self._black_player]
    
    @property
    def timeline(self) -> GameResultStack:
        return self._timeline
    
    @property
    def current_result(self) -> Optional[GameUpdate]:
        return self._timeline.last_result
        
