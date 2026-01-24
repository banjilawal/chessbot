from chess.square import Square
from chess.system import LoggingLevelRouter
from chess.token import Token


class Attack:
    
    @classmethod
    @LoggingLevelRouter
    def execute(cls, attacker: Token, target_square: Square):