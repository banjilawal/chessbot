from typing import TYPE_CHECKING, List

from chess.coord import Coord

if TYPE_CHECKING:
  from chess.piece.piece import Piece

class Discovery:
  """
  An immutable record of a piece found during play.

  A `Discovery` is created when a `Piece` detects another piece (friend or enemy) at a given `Square``.
  It captures the essential identifying information about the discovered piece without holding a direct
  reference, ensuring immutability and safe storage within search logs or decision-making structures.

  `Discovery` objects are used to record what a piece has observed during scanning, moving, or event
  attempts. They provide enough detail (identity, team, rank, ransom value, and position) for evaluation
  by search and decision engines, while remaining lightweight and detached from the full `Piece` object.

  Attributes:
    _id (int): The unique identifier of the discovered piece.
    _name (str): The name of the discovered piece (e.g., "Pawn", "Queen").
    _team_id (int): The identifier of the team to which the discovered piece belongs.
    _ransom (int): The ransom (or value) associated with the discovered piece's rank.
    _rank_name (str): The rank name of the discovered piece (e.g., "Knight", "Bishop").
    _coord (Coord): The board coord where the discover was observed.
  """

  _id: int
  _name: str
  _team_id: int
  _ransom: int
  _rank_name: str
  _coord: Coord

  def __init__(self, piece: 'Piece'):
    self._id = piece.id
    self._name = piece.name
    self._ransom = piece.rank.ransom
    self._rank_name = piece.rank.name
    self._team_id = piece.team.id
    self._coord = piece.current_position

  @property
  def id(self) -> int:
    return self._id

  @property
  def name(self) -> str:
    return self._name

  @property
  def team_id(self):
    return self._team_id

  @property
  def rank_name(self) -> str:
    return self._rank_name

  @property
  def ransom(self):
    return self._ransom

  @property
  def coord(self) -> Coord:
    return self._coord

  def __eq__(self, other):
    """We have to use the coord because the id """
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance('Discovery', other):
      return False
    return self._id == other.id and self._coord == other.coord


  def __str__(self):
    return (
      f"Discovery[id:{self._id} "
      f"name:{self._name} "
      f"rank:{self._rank_name} "
      f"ransom:{self._ransom} "
      f"coord:{self._coord}"
    )











