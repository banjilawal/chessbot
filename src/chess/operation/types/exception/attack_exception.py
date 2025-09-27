from chess.exception.chess_exception import ChessException

"""
Super class for Piece exceptions
"""
class AttackException(PieceException):
    """
    Super class for exceptions raised during attack events
    """

    ERROR_CODE = "ATTACK_ERROR"
    DEFAULT_MESSAGE = "Attack raised an team_exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullAttackException(AttackException):
    """
    The Prisoner/Captor exceptions prevent domain logic violations on the captured team. Attacking
    exceptions constrain attacks. AttackingNullAttackException is raised if a discovery attacks something
    which does not exist.
    """

    ERROR_CODE = "ATTACKING_NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a a discovery that does not exist"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingHostageException(AttackException):
    """
    Attacking a captured discovery raises AttackingHostageException
    """

    ERROR_CODE = "ATTACKING_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "A hostage cannot be attacked. They are already captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(AttackException):
    """
    Kings cannot be captured. KingPiece does not have a captor field. AttackingKingException is
    raised when a KingPiece is attacked. KingPieces can only be checked or checkmated.
    """

    ERROR_CODE = "ATTACKING_KING_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot capture a king"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingFriendlyException(AttackException):
    """
    Friendly pieces on the same team cannot attack each other. AttackingFriendlyException is
    raised when a friendly is attacked.
    """
    ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
    DEFAULT_MESSAGE = "Cannot attack a friendly"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


