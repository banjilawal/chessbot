from chess.exception.negative_id_exception import ChessException


class SquareException(ChessException):
    default_message = "An error occurred in p chess square"

class MissingSquareException(SquareException):
    default_message = "Chess square does not exist. Passing null square not allowed."

class OccupationBlockedException(SquareException):
    default_message = "The chess square is occupied by another friendly captor."

class OccupationCleanupException(SquareException):
    default_message = "An occupation clean up task failed. Entities have inconsistent states."

class VacateCleanUpException(SquareException):
    default_message = "An vacate clean up task failed. Entities have inconsistent states."

class InaccurateOccupationStatusException(SquareException):
    default_message = "The occupation test_outcome is inaccurate"