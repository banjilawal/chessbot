from typing import cast

from chess.arena import Arena
from chess.system import Dyad

from chess.team import Team


class ArenaTeamDyad(Dyad[Arena, Team]):
    
    def __init__(self, primary: Arena, satellite: Team):
        super().__init__(primary=primary, satellite=satellite)
        
    @property
    def primary(self) -> Arena:
        return cast(Arena, self.dyad_primary)
        
    @property
    def satellite(self) -> Team:
        return cast(Team, self.dyad_satellite)
    