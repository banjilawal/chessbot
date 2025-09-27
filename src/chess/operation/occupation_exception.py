from chess.exception.chess_exception import ChessException

"""
Thrown if square does not contain a friendly and Event.RECORD_ENCOUNTER event was in the outcome 
"""
class CorruptRecordEventException(ChessException):
    """
    Thrown if square does not contain a friendly and Event.RECORD_ENCOUNTER event was in the outcome
    """
    ERROR_CODE = "MARK_OBSTRUCTION_EVENT_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain a friendly. Granting RECORD_ENCOUNTER was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Thrown if square does not contain a and enemy and Event.ATTACK was iin the outcome 
"""
class AttackPermissionInconsistencyException(ChessException):
    """
    Thrown if square does not contain a and enemy and Event.ATTACK was iin the outcome
    """
    ERROR_CODE = "ATTACK_PERMISSION_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain an enemy. Granting ATTACK_PERMISSION was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class OccupationException(ChessException):
    ERROR_CODE = "OCCUPATION_ERROR"
    DEFAULT_MESSAGE = "An occupation team_exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class OccupyNullSquareException(ChessException):
    ERROR_CODE = "OCCUPY_NULL_SQUARE_EXCEPTION"
    DEFAULT_MESSAGE = "Cannot occupy a square which does not exist"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class FriendlyOccupantException(OccupationException):
    ERROR_CODE = "FRIENDLY_OCCUPANT_ERROR"
    DEFAULT_MESSAGE = "A friendly is already occupying the square"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"






class KingCheckStateException(PieceException):
    """
    This really should not be an team_exception. Its really supposed to be a warning to the king
    when its in check. This team_exception should never be thrown but its messages can be handy.
    """

    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead discovery cannot attack"


class KingCheckMateStateException(PieceException):
    """
    This really should not be an team_exception. Its really supposed to be a warning to indicate the
    game is over because the king is checkmated. This team_exception should never be thrown but its
    messages can be handy.
    """

    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"


class RemoveCombatantException(TeamException):
    """
    If Team.remove_captured_combatant fails this team_exception is raised.
    """

    ERROR_CODE = "REMOVE_CAPTURED_COMBATANT_ERROR"
    DEFAULT_MESSAGE = "Could not remove the captured hostage from the roster"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"