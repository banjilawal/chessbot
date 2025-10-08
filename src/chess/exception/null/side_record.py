from chess.exception import NullException


class NullSideRecordException(NullException):
  """
  Raised if team Commander's sides_played property is null.
  """

  ERROR_CODE = "NULL_TEAM_HISTORY_ERROR"
  DEFAULT_MESSAGE = f"TeamHistory cannot be null"


  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)


  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"