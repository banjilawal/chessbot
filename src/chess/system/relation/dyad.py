from typing import TypeVar

P = TypeVar("P")
S = TypeVar("S")


class Dyad:
    _primary: P
    _satellite: S
    
    def __init__(self, primary: P, satellite: S):
        self._primary = primary
        self._satellite = satellite
        
    @property
    def dyad_primary(self) -> P:
        return self._primary
    
    @property
    def dyad_satellite(self) -> S:
        return self._satellite