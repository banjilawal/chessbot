# src/model/software/subscriber/model/software.py

"""
Module: model.software.subscriber.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from typing import List, Optional

from model.agent import PlayerAgent
from model.arena import Arena
from model.software.subscriber import Snapshot, SubscriberTimeline

from model.software.license import SoftwareLicense


class Subscriber:
    """
    Role:Controller

    Responsibilities:
    Interface players use to change the Arena's software.

    Super Class:
    None

    # PROVIDES:
    Subscriber

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (Player)
        *   black_player (Player)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _first_name: str
    _last_name: str
    _email: str
    _licenses: List[SoftwareLicense]
    
    def __init__(
            self,
            id: int,
            first_name: str,
            last_name: str,
            email: str,
            licenses: Optional[List[SoftwareLicense]] | None = None,
    ):
        """
        Args:
            id: int,
            first_name: str,
            last_name: str,
            email: str,
            licenses: Optional[List[SoftwareLicense]
        """
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._licenses = licenses or []
    
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
    def timeline(self) -> SubscriberTimeline:
        return self._timeline
    
    @property
    def previous_move(self) -> Optional[Snapshot]:
        return self._timeline.previous_move()
