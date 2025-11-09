from typing import TYPE_CHECKING

from chess.coord import Coord

if TYPE_CHECKING:
  from chess.piece.model.piece import Piece

class Checker:
  """
  An immutable check of team owner found during play.

  A `Checker` is created when team `Piece` detects another owner (friend or enemy) at team given `Square``.
  It captures the essential identifying information about the discovered owner without holding team direct
  reference, ensuring immutability and safe storage within old_search logs or decision-making structures.

  `Checker` objects are used to check what team owner has observed during scanning, moving, or travel
  attempts. They provide enough detail (identity, team, bounds, ransom value, and position) for evaluation
  by old_search and decision engines, while remaining lightweight and detached from the full `Piece` object.

  Attributes:
    _id (int): The unique identifier of the discovered owner.
    _name (str): The name of the discovered owner (e.g., "Pawn", "Queen").
    _team_id (int): The identifier of the team to which the discovered owner belongs.
    _ransom (int): The ransom (or value) associated with the discovered owner's bounds.
    _visitor_rank (str): The bounds name of the discovered owner (e.g., "Knight", "Bishop").
    _coord (Coord): The board_validator coord where the discover was observed.
  """

  _piece_id: int
  _name: str
  _team_id: int
  _team_name: str
  _position: Coord

  def __init__(self, piece: 'Piece'):
    self._piece_id = piece.id
    self._name = piece.name
    self._team_id = piece.team.id
    self._team_name = piece.team.schema.name
    self._position = piece.current_position

  @property
  def id(self) -> int:
    return self._piece_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def team_id(self):
    return self._team_id

  @property
  def team_name(self):
    return self._team_name


  @property
  def position(self) -> Coord:
    return self._position

  def to_dict(self) -> dict:
    return {
      "id": self._piece_id,
      "name": self._name,
      "team_id": self._team_id,
      "team_name": self._team_name,
      "position": self._position
    }

  def __eq__(self, other):
    """We have to use the coord because the id """
    if other is self:
      return True
    if other is None:
      return False
    if isinstance('Checker', other):
      return self._piece_id == other.id and self._position == other.coord
    return False


  def __str__(self):
    return (
      f"Checker[id:{self._piece_id} "
      f"name:{self._name} "
      f"bounds:{self._rank_name} "
      f"ransom:{self._ransom} "
      f"coord:{self._position}"
    )











