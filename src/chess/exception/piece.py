from chess.exception.base import ChessException

"""
Super class for Piece exceptions
"""
class PieceException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """

    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Exception for handling a piece which does not have a coordinate
"""
class PieceCoordinateException(PieceException):
    """
    If a piece does not have a coordinate until its place on the chess board. This exception prevents
    chess pieces not on the board from moving.
    """

    ERROR_CODE = "PIECE_NO_COORDINATE_ERROR"
    DEFAULT_MESSAGE = "Piece is not on the board. it has no coordinate"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Raised if attempting to move a captured piece
"""
class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured combatant will raise this exception. KingPiece cannot be captured.
    """

    ERROR_CODE = "CAPTURED_PIECE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Attempting to change captor piece to null if its not null
"""
class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. This exception is raised if an attempt
    """
    ERROR_CODE = "CAPTURED_PIECE_RELEASE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor from not null to null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Prevents Combatant.captor to null
"""
class NullCaptorException(PieceException):
    """
    Cannot set Combatant.captor to null
    """

    ERROR_CODE = "CAPTURED_PIECE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullPieceException(PieceException):
    ERROR_CODE = "ATTACKING_NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingPrisonerException(PieceException):
    ERROR_CODE = "ATTACKING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a piece already captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(PieceException):
    ERROR_CODE = "ATTACKING_KING_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot capture a king"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingFriendlyException(PieceException):
    ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
    DEFAULT_MESSAGE = "Cannot attack a friendly"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DoublePromotionException(PieceException):

    """
    Only a piece can be doubly promoted. DoublePromotionException is a PieceException
    not a RankException.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted. It cannot be promoted again"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingCheckStateException(PieceException):
    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead piece cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class KingCheckMateStateException(PieceException):
    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class MappingSelfException(PieceException):
    ERROR_CODE = "MAPPING_SELF_ERROR"
    DEFAULT_MESSAGE = "You cannot add yourself to the map"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"