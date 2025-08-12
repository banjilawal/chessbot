from chess.exception.exception import ChessException


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


"""
RankValidationException Hierarchy
"""
class RankValidationException(ValidationException):
    default_message = f"Rank {ValidationException.default_message}"

class KingRankValidationException(RankValidationException):
    default_message = f"KingRank {RankValidationException.default_message}"

class PawnRankValidationException(RankValidationException):
    default_message = f"PawnRank {RankValidationException.default_message}"

class CastleRankValidationException(RankValidationException):
    default_message = f"CastleRank {RankValidationException.default_message}"

class BishopRankValidationException(RankValidationException):
    default_message = f"BishopRank {RankValidationException.default_message}"

class KnightRankValidationException(RankValidationException):
    default_message = f"KnightRank {RankValidationException.default_message}"

class QueenRankValidationException(RankValidationException):
    default_message = f"QueenRank {RankValidationException.default_message}"
