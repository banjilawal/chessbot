from abc import ABC
from typing import Optional, cast, TYPE_CHECKING

from chess.coord import CoordValidator
from assurance import IdValidator, NameValidator
from chess.system import auto_id
from chess.team import Team
from chess.piece import Piece
from chess.commander import CommandHistory

if TYPE_CHECKING:
  pass

@auto_id
class Commander(ABC):
  _name: str
  _teams: CommandHistory
  _current_team: Optional['Team']


  def __init__(self, name: str):

    # id_validation = IdValidator.validate(commander_id)
    # if not id_validation.is_success():
    #   raise id_validation.exception

    name_validation = NameValidator.validate(name)
    if not name_validation.is_success():
      raise name_validation.exception

    # self._id = cast(int, id_validation.payload)
    self._name = cast(str, name_validation.payload)
    self._teams = CommandHistory()

    self._current_team = self._teams.current_team
  #
  #
  # @property
  # def id(self) -> int:
  #   return self._id
  #

  @property
  def name(self) -> str:
    return self._name


  @property
  def teams(self) -> CommandHistory:
    return self._teams


  @property
  def current_team(self) -> Optional['Team']:
    return self._teams.current_team


  @name.setter
  def name(self, name: str):
    self._name = name


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Commander):
      return False
    return self.id == other.id


  def __str__(self):
    total_games = self.teams.size()
    total_games_str = f"total games:{total_games}" if total_games > 0 else ""

    current_side = "" if self._current_team is None else \
      f" curren_team:[{self._current_team.id}, {self._current_team.scheme.color}"
    return (
      f"Owner[id:{self._id}"
      f" name:{self._name}"
      f"{current_side}"
      f"{total_games_str}"
      f"]"
    )


  def move_piece(self, piece_name:str, destination:Coord):
    method = "Commander.move_piece"

    try:
      validation = NameValidator.validate(piece_name)
      if not validation.is_success():
        raise validation.exception

      result = self._current_team.find_piece_by_name(piece_name)
      if not result.is_success():
        raise result.exception

      piece = cast(Piece, result.payload)

      # if discover is None:
      #   raise PieceNotFoundException(
      #     f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE} at index {array_index}"
      #   )

      if piece.current_position is None:
        raise PieceCoordNullException(f"{method}: {PieceCoordNullException.DEFAULT_MESSAGE}")

      if isinstance(piece, CombatantPiece) and piece.captor is not None:
        raise PrisonerEscapeException(f"{method}: Cannot move {piece.name} it has been captured.")

      validation = CoordValidator.validate(destination)
      if not validation.is_success():
        raise validation.exception

      if piece.current_position == destination:
        raise AlreadyAtDestinationException(f"{method}: {AlreadyAtDestinationException.DEFAULT_MESSAGE}")

      piece.rank.walk(piece=piece, destination=destination)

    except (NullPieceException, ConflictingTeamException) as e:
      raise AddPieceException(f"{method}: {AddPieceException.DEFAULT_MESSAGE}")