from chess.persona import Persona
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook


class RosterTable:
    _table: {Rank: int}
    
    def __init__(self):
        _table = {
            King: Persona.KING.quota,
            Pawn: Persona.PAWN.quota,
            Knight: Persona.KNIGHT.quota,
            Bishop: Persona.BISHOP.quota,
            Rook: Persona.ROOK.quota,
            Queen: Persona.QUEEN.quota,
        }
        
    def quota_not_filled(self, persona: Persona) -> bool:
        return self._table.get(persona) > 0
    
    def quota_filled(self, persona: Persona) -> bool:
        return self._table.get(persona) <= 0
    
    def decrease_quota(self, rank: Rank):
        quota = self._table.get(rank) - 1
        self._table.rank = quota
        
    def get_quota(self, rank) -> int:
        return self._table.get(rank)
        

        
    