
class KingPiece(Piece):
  """A concrete subclass representing team king piece."""
  _is_checked: bool
  _is_checkmated: bool

  def __init__(self,name: str, rank: 'Rank', team: 'Team'):
    super().__init__(name, rank, team)
    self._is_checked = False
    self._is_checkmated = False


  @property
  def is_checked(self) -> bool:
    return self._is_checked

  @property
  def is_checkmated(self) -> bool:
    return self._is_checkmated

  @is_checked.setter
  def is_checked(self, is_checked: bool):
    self._is_checked = is_checked

  @is_checkmated.setter
  def is_checkmated(self, is_checkmated: bool):
    if self._is_checked:
      self._is_checkmated = is_checkmated
    else:
      raise Exception("Cannot set checkmated status if not checked")


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, KingPiece):
      return self.id == other.id


class CombatantPiece(Piece):
  _captor: Optional[Piece]

  def __init__(self, name: str, rank: 'Rank', team: 'Team'):
    super().__init__(name, rank, team)
    self._captor = None


  @property
  def captor(self) -> Optional[Piece]:
    return self._captor


  @captor.setter
  def captor(self, captor: Piece):
    self._captor = captor


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, CombatantPiece):
      return self.id == other.id



