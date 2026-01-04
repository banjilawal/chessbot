from chess.persona import Persona, PersonaService
from chess.system import CalculationResult
from chess.system.result import Result
from chess.team import Team
from chess.token import TokenContext


class RosterTable:
    _table: {Persona: int}
    
    def __init__(self):
        _table = {
            Persona.PAWN: 0,
            Persona.KNIGHT: 0,
            Persona.BISHOP: 0,
            Persona.ROOK: 0,
            Persona.QUEEN: 0,
            Persona.KING: 0,
        }
        
    def quota_not_filled(self, persona: Persona) -> bool:
        return self._table.get(persona) < persona.quota
    
    def quota_filled(self, persona: Persona) -> bool:
        return self._table.get(persona) == persona.quota
    
    # def increment_count(self, persona: Persona) -> Result:
    #     if self.quota_filled(persona):

        

        
    