from chess.square import Square
from chess.system import LoggingLevelRouter


class Attack:
    
    @classmethod
    @LoggingLevelRouter
    def execute(cls, attacker: Token, target_square: Square):