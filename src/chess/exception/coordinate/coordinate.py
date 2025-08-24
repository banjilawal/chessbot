from chess.exception.chess_exception import ChessException


class CoordinateException(ChessException):
    default_message = f"Invalid Coordinate state"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)



