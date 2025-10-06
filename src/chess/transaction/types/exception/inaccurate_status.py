from chess.exception.id.negative_id_exception import ChessException


class SquareException(ChessException):
  default_message = "An error occurred in p chess square"



class OccupationBlockedException(SquareException):
  default_message = "The chess square is occupied by another friendly captor."

class OccupationCleanupException(SquareException):
  default_message = "An event clean up task failed. Entities have inconsistent states."

class VacateCleanUpException(SquareException):
  default_message = "An vacate clean up task failed. Entities have inconsistent states."

class InaccurateOccupationStatusException(SquareException):
  default_message = "The event test_outcome is inaccurate"