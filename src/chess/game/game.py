# src/chess/game/game.py

"""
Module: chess.game.game
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import List, Optional

from chess.agent import PlayerAgent
from chess.arena import Arena
from chess.game import Snapshot, GameTimeline, GameTimelineException


class Game:
    """
    # ROLE: Controller

    # RESPONSIBILITIES:
    Interface players use to change the Arena's state.

    # PARENT:
    None

    # PROVIDES:
    Game

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (PlayerAgent)
        *   black_player (PlayerAgent)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _arena: Arena
    _white_player: PlayerAgent
    _black_player: PlayerAgent
    _timeline: GameTimeline
    
    def __init__(self, id: int, white_player: PlayerAgent, black_player: PlayerAgent, arena: Arena):
        self._id = id
        self._arena = arena
        self._white_player = white_player
        self._black_player = black_player
        self._timeline = GameTimeline()
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def white_player(self) -> PlayerAgent:
        return self._white_player
    
    @property
    def black_player(self) -> PlayerAgent:
        return self._black_player
    
    @property
    def players(self) -> List[PlayerAgent]:
        return [self._white_player, self._black_player]
    
    @property
    def timeline(self) -> GameTimeline:
        return self._timeline
    
    @property
    def previous_move(self) -> Optional[Snapshot]:
        return self._timeline.previous_move()
