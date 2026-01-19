from chess.coord import Coord
from chess.token import CombatantToken, Token


class HostageManifest:
    _id: int
    _victor: Token
    _prisoner: CombatantToken
    _capture_location: Coord
    
    def __init__(self, id: int, victor: Token, prisoner: CombatantToken):
        self._id = id
        self._victor = victor
        self._prisoner = prisoner
        self._capture_location = self._victor.current_position
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victor(self) -> Token:
        return self._victor
    
    @property
    def prisoner(self) -> CombatantToken:
        return self._prisoner
    
    @property
    def capture_location(self) -> Coord:
        return self._capture_location
        
    