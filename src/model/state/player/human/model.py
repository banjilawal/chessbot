# src/model/state/player/human/model/state.py

"""
Module: model.state.player.human.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Player


class HumanPlayer(Player):
    """
    Role:Controller

    Responsibilities:
    1.  Forward requests and commands from a Human owner to the Game model.
    2.  Forward movement commands from the person playing to their pieces on the Board.
    
    Super Class:
        *   Player

    Provides:

    
    # INHERITED ATTRIBUTES:
        *   See Player class for inherited attributes.
    """
    
    def __init__(
            self,
            id: int,
            name: str,
            teams: UniqueTeamDataService = UniqueTeamDataService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   schema (str)
            *   games (UniqueGameDataService)
            *   teams (TeamDatabase)

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name, games=games, teams=teams)
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, HumanPlayer):
                return True
        return False
    
    def __hash__(self):
        return hash(self.id)
