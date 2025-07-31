from chess.common.exceptions import ChessException


class SquareException(ChessException):
    default_message = "An error occurred in a chess square"

class MissingSquareException(SquareException):
    default_message = "Chess square does not exist. Passing null square not allowed."

class OccupationBlockedException(SquareException):
    default_message = "The chess square is occupied by another friendly piece."

class OccupationCleanupException(SquareException):
    default_message = "An occupation clean up task failed. Entities have inconsistent states."

class VacateCleanUpException(SquareException):
    default_message = "An vacate clean up task failed. Entities have inconsistent states."

class InaccurateOccupationStatusException(SquareException):
    default_message = "The occupation status is inaccurate"