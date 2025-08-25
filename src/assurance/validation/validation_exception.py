from chess.exception.base.negative_id_exception import ChessException


class ValidationException(ChessException):
    default_message = f"Validation failed"

class IdValidationException(ValidationException):
    default_message = f"Id {ValidationException.default_message}"

class SquareValidationException(ValidationException):
    default_message = f"Square {ValidationException.default_message}"

class CoordinateValidationException(ValidationException):
    default_message = f"Coordinate {ValidationException.default_message}"

class ChessPieceValidationException(ValidationException):
    default_message = f"ChessPiece {ValidationException.default_message}"
