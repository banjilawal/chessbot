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


class PieceCoordNullException(PieceException):
    """
    PieceCoordNullException gets thrown if a piece with an empty coordinate stack attempts to move.
    If piece.positions.is_empty == True then the piece is not on the board so it cannot be moved.
    """

    ERROR_CODE = "PIECE_NO_COORDINATE_ERROR"
    DEFAULT_MESSAGE = "Piece is not on the board. Cannot move a piece with len(piece.positions) == 0"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AlreadyAtDestinationException(PieceException):
    """
    If a piece's destination is its current position raise AlreadyAtDestination.
    """

    ERROR_CODE = "ALREADY_AT_DESTINATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already at the destination."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured combatant raises PrisonerEscapeException. This only applies to combatant pieces
    """

    ERROR_CODE = "MOVING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot move a captured piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_piece.captor != null to combatant_piece.captor = None
    """

    ERROR_CODE = "RELEASING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor to null once it has been set to an enemy piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class NullCaptorException(PieceException):
    """
    If the captor field has not been set its already null. I really want to prevent nulls being passed to
    Combatant.captor. This is for consistency. I don't just want an if that returns to caller when
    Combatant.captor == None and the caller tries to send null again. I want an exception to catch it. The
    exception name needs improvement.
    """

    ERROR_CODE = "CAPTURED_PIECE_ESCAPE_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullPieceException(PieceException):
    """
    The Prisoner/Captor exceptions prevent domain logic violations on the captured side. Attacking
    exceptions constrain attacks. AttackingNullPieceException is raised if a piece attacks something
    which does not exist.
    """

    ERROR_CODE = "ATTACKING_NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a a piece that does not exist"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingPrisonerException(PieceException):
    """
    AttackingPrisonerException is raised when a captured piece is attacked again."
    """

    ERROR_CODE = "ATTACKING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a piece already captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(PieceException):
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


class AttackingFriendlyException(PieceException):
    """
    Friendly pieces on the same side cannot attack each other. AttackingFriendlyException is
    raised when a friendly is attacked.
    """
    ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
    DEFAULT_MESSAGE = "Cannot attack a friendly"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DoublePromotionException(PieceException):
    """
    If a piece with rank in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess piece.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class SelfEncounterException(PieceException):
    """
    Prevents the piece from adding itself to the list of encounters.
    """

    ERROR_CODE = "SELF_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = "Piece cannot create an Encounter entry on itself"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class KingCheckStateException(PieceException):
    """
    This really should not be an exception. Its really supposed to be a warning to the king
    when its in check. This exception should never be thrown but its messages can be handy.
    """

    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead piece cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingCheckMateStateException(PieceException):
    """
    This really should not be an exception. Its really supposed to be a warning to indicate the
    game is over because the king is checkmated. This exception should never be thrown but its
    messages can be handy.
    """

    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


