from chess.exception.chess_exception import ChessException


class SideException(ChessException):
    """
    Super class for exception raised by a Side object when its internal fields or methods
    """

    ERROR_CODE = "SIDE_ERROR"
    DEFAULT_MESSAGE = "Side raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class SideSearchException(SideException):
    """
    If a search parameter fails validation or sanity checks a SideSearchException is raised.
    """

    ERROR_CODE = "SIDE_SEARCH_ERROR"
    DEFAULT_MESSAGE = "search parameter raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ConflictingSideException(SideException):
    """
    If a piece that's already on one side (piece.side == not None) tries joining
    another ConflictingSideException is raised.
    """

    ERROR_CODE = "CONFLICTING_SIDE_ERROR"
    DEFAULT_MESSAGE = "piece is on a different side. Cannot join this one"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AddPieceException(SideException):
    """
    Raised if piece could not be added to the side's roster
    """

    ERROR_CODE = "ADD_PIECE_ERROR"
    DEFAULT_MESSAGE = "Could not add the piece, an exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RemoveCombatantException(SideException):
    """
    If Side.remove_captured_combatant fails this exception is raised.
    """

    ERROR_CODE = "REMOVE_CAPTURED_COMBATANT_ERROR"
    DEFAULT_MESSAGE = "Could not remove the captured hostage from the roster"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

