from chess.system import ChessException

__all__ = [
    "GameException",
]


class GameException(ChessException):
    """
    # ROLE
    Exception, Debugging
    
    # RESPONSIBILITIES
    1.  Super class af exceptions raised by Ga Game object's properties and instance methods.
    2.  Parent class of Game build/validation exceptions.
    3.  Parent class of GameContext and GameSearch exceptions.
    4.  Parent class of GameService and GameDataService exceptions.
    
    # PROVIDES
      * GameException
      
    # ATTRIBUTES
        *   ERROR_CODE (str)
        *   DEFAULT_MESSAGE (str)
        *   ex (Exception)
    """
    ERROR_CODE = "GAME_ERROR"
    DEFAULT_MESSAGE = "Game raised an exception."
