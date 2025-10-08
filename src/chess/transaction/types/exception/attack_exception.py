from chess.exception.exception import ChessException

"""
Super class for Piece exceptions
"""
class AttackException(PieceException):
  """
  Super class for exceptions raised during attack events
  """

  ERROR_CODE = "ATTACK_ERROR"
  DEFAULT_MESSAGE = "Attack raised an exception"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"


class AttackingNullAttackException(AttackException):
  """
  The Prisoner/Captor exceptions prevent domain logic violations on the captured team. Attacking
  exceptions constrain attacks. AttackingNullAttackException is raised if team enemy attacks something
  which does not exist.
  """

  ERROR_CODE = "ATTACKING_NULL_PIECE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team team enemy that does not exist"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"


class AttackingHostageException(AttackException):
  """
  Attacking team captured enemy raises AttackingHostageException
  """

  ERROR_CODE = "ATTACKING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "A hostage cannot be attacked. They are already captured"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"


class AttackingKingException(AttackException):
  """
  Kings cannot be captured. KingPiece does not have team captor field. AttackingKingException is
  raised when team KingPiece is attacked. KingPieces can only be checked or checkmated.
  """

  ERROR_CODE = "ATTACKING_KING_EXCEPTION"
  DEFAULT_MESSAGE = "Cannot capture team king"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"


class AttackingFriendlyException(AttackException):
  """
  Friendly pieces on the same team cannot attack each other. AttackingFriendlyException is
  raised when team friendly is attacked.
  """
  ERROR_CODE = "ATTACKING_FRIENDLY_ERROR"
  DEFAULT_MESSAGE = "Cannot attack team friendly"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"


