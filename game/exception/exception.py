# First, define your custom exceptions (in a separate exceptions.py file)
class GameError(Exception):
    """Base exception for all game-related errors"""
    pass

class InvalidBoardError(GameError):
    """Raised when the board is not valid"""
    pass

class InvalidNumberOfRowsError(GameError):
    """Raised when the number of rows is not valid"""
    pass

class InvalidNumberOfColumnsError(GameError):
    """Raised when the number of columns is not valid"""
    pass

class InvalidIdError(GameError):
    """Raised when an id iss not valid for the game"""
    pass

class InvalidFigureHeightError(GameError):
    """Raised when a figure's height is not valid"""
    pass

class InvalidFigureLengthError(GameError):
    """Raised when a figure's height is not valid"""
    pass

class FigureAreaBelowLimitError(GameError):
    """Raised when a figure's area is below the limit"""

class InvalidIdError(GameError):
    """Raised when an id iss not valid for the game"""
    pass

class InvalidSquareError(GameError):
    """Raised when attempting to interact with an invalid square"""
    pass

class NullSquareEntryError(GameError):
    """Raised when attempting to enter a square that does not exist"""
    pass

class OccupiedSquareEntryError(GameError):
    """Raised when attempting to enter an already occupied square"""
    pass

class SquareNotVacatedError(GameError):
    """Raised when attempting to leave a square that is not vacated"""

class SelfOccupiedSquareError(GameError):
    """Raised when attempting to enter a square already occupied by self"""
    pass

class SquareOwnershipError(GameError):
    """Raised when attempting to leave a square owned by a different figure."""
    pass

class NoSquareToLeaveError(GameError):
    """Raised when attempting to leave a square while not occupying any"""
    pass

class NegativeRowError(GameError):
    """Raised GameBoardSquare cannot be on a negative row."""
    pass

class NegativeColumnError(GameError):
    """GameBoardSquare cannot be on a negative column."""
    pass
