from chess.exception import ChessException, NullException, ValidationException

__all__ = [
  'RankException',

# === RANK VALIDATION EXCEPTIONS ===
  'NullRankException',
  'InvalidRankException',
  'UnRecognizedConcreteRankException',

# === RANK SUBCLASS VALIDATION EXCEPTIONS ===
  'InvalidKingException',
  'InvalidPawnException',
  'InvalidKnightException',
  'InvalidBishopException',
  'InvalidRookException',
  'InvalidQueenException',

# === RANK BUILD EXCEPTIONS ===

# === RANK MOVING EXCEPTIONS ===
  'MovingException',
  'KingMovingException',
  'PawnMovingException',
  'KnightMovingException',
  'BishopMovingException',
  'RookMovingException',
  'QueenMovingException'
]

class RankException(ChessException):
  ERROR_CODE = "RANK_ERROR"
  DEFAULT_MESSAGE = "Rank raised an exception."

# === RANK VALIDATION EXCEPTIONS ===
class NullRankException(RankException, NullException):
  ERROR_CODE = "NULL_RANK_ERROR"
  DEFAULT_MESSAGE = "Rank cannot be null"

class InvalidRankException(RankException, ValidationException):
  ERROR_CODE = "RANK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Rank validate failed"

class UnRecognizedConcreteRankException(RankException):
  ERROR_CODE = "UNRECOGNIZED_CONCRETE_RANK_ERROR"
  DEFAULT_MESSAGE = "This concrete subclass of Rank is not recognized"


# === RANK SUBCLASS VALIDATION EXCEPTIONS ===
class InvalidKingException(InvalidRankException):
  ERROR_CODE = "KING_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "King validate failed."

class InvalidPawnException(InvalidRankException):
  ERROR_CODE = "PAWN_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Pawn validate failed."

class InvalidKnightException(InvalidRankException):
  ERROR_CODE = "KNIGHT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Knight validate failed."

class InvalidBishopException(InvalidRankException):
  ERROR_CODE = "BISHOP_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Bishop validate failed."

class InvalidRookException(InvalidRankException):
  ERROR_CODE = "ROOK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Rook validate failed."

class InvalidQueenException(InvalidRankException):
  ERROR_CODE = "QUEEN_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Queen validate failed."


# === RANK MOVING EXCEPTIONS ===
class MovingException(RankException):
  ERROR_CODE = "RANK_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid move."

class BishopMovingException(RankException):
  ERROR_CODE = "BISHOP_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid bishop move"

class KingMovingException(RankException):
  ERROR_CODE = "KING_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid king move"

class KnightMovingException(RankException):
  ERROR_CODE = "KNIGHT_MOVING_ERROR"
   DEFAULT_MESSAGE = "Invalid knight move"

class PawnMovingException(RankException):
    ERROR_CODE = "PAWN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid pawn move"

class QueenMovingException(RankException):
    ERROR_CODE = "QUEEN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid queen move"

class RookMovingException(RankException):
    ERROR_CODE = "ROOK_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid rook move"




