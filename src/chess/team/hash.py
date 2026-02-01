from typing import Dict

from chess.system import GameColor
from chess.team import Team


class TeamHash:
    _white_team: Team
    _black_team: Team
    
    def __init__(self, white_team: Team, black_team: Team):
        self._white_team = white_team
        self._black_team = black_team
        
        @property
        def white_team(self) -> Team:
            return self._white_team
        
        @property
        def black_team(self) -> Team:
            return self._black_team
        
        @property
        def hash_table(self) -> Dict[GameColor, Team]:
            return {
                GameColor.WHITE: self._white_team,
                GameColor.BLACK: self._black_team
            }
        
    