from chess.exception import ChessException, NullException, BuilderException, ValidationException

__all__ = [
    'BoardException',
    'BoardRollBackException',

    # === BOARD VALIDATION EXCEPTIONS ===
    'NullBoardException',

    # === BOARD BUILDER EXCEPTIONS ===
    'BoardBuilderException',
    
    # === PIECE ADDITION/REMOVAL EXCEPTIONS ===
    'BoardPieceAdditionFailedException',
    'BoardPieceRemovalFailedException',

    # === PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK ===
    'FailedPieceAdditionRolledBackException',
    'FailedPieceRemovalRolledBackException',

]

class BoardException(ChessException):
    """
    Super class of all exceptions a Board object raises. Do not use directly. Subclasses give details useful
    for debugging. This class exists primarily to allow catching all board exceptions
    """
    ERROR_CODE = "BOARD_ERROR"
    DEFAULT_MESSAGE = "Board raised an err"

class BoardRollBackException(BoardException):
    """
    Super class for exceptions that require a rollback to maintain board integrity.
    """
    ERROR_CODE = "BOARD_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Board raised an err. Transaction rollback performed."


# === BOARD VALIDATION EXCEPTIONS ===
class NullBoardException(BoardException, NullException):
    """Raised if an entity, method, or operation requires a board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be null"
    
class InvalidBoardException(BoardException, ValidationException):
    """
    Raised by BoardValidator if board fails sanity checks. Exists primarily to catch all exceptions raised
    validating an existing board
    """
    ERROR_CODE = "BOARD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Board validation failed"
    
# === BOARD BUILDER EXCEPTIONS ===
class BoardBuilderException(BoardException, BuilderException):
    """
    Raised when BoardBuilder encounters an err while building a team. Exists primarily to catch all
    exceptions raised build a new board
    """
    ERROR_CODE = "BOARD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "BoardBuilder raised an err. Board creation failed."
    

# === PIECE ADDITION/REMOVAL EXCEPTIONS ===
class BoardPieceAdditionFailedException(BoardException):
    """Raised if the board fails to remove a piece from itself"""
    ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "Board failed to add the piece"

class BoardPieceRemovalFailedException(BoardException):
    """Raised if the board fails to remove a piece from itself"""
    ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Board failed to remove the piece"

# === PIECE ADDITION/REMOVAL EXCEPTIONS WITH ROLLBACK ===
class FailedPieceAdditionRolledBackException(BoardRollBackException):
    """
    Raised if a transaction failed to add a piece to the board.The transaction was
    rolled back before raising this err.
    """
    """Raised if the board fails to remove a piece from itself"""
    ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Could not remove a piece from the board. Transaction rollback performed."
    )

class FailedPieceRemovalRolledBackException(BoardRollBackException):
    """
    Raised if a  transaction failed to remove a piece from the board's list of pieces.
    The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Could not remove a piece from the board. Transaction rollback performed."
    )


class IncompleteBoardTransactionException(BoardException):
    ERROR_CODE = "BOARD_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "The board is an inconsistent state. Transaction failed."