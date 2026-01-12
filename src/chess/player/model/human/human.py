# src/chess/model/human/human.py

"""
Module: chess.model.human.human
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import Player
from chess.team import UniqueTeamDataService


class HumanPlayer(Player):
    """
    # ROLE: Controller

    # RESPONSIBILITIES:
    1.  Forward requests and commands from a Human owner to the Game model.
    2.  Forward movement commands from the person playing to their pieces on the Board.
    
    # PARENT:
        *   Player

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
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
            *   name (str)
            *   games (UniqueGameDataService)
            *   teams (UniqueTeamDataService)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, games=games, teams=teams)
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, HumanPlayer):
                return True
        return False
    
    def __hash__(self):
        return hash(self.id)
