from typing import Optional, List
from chess.rank import Queen, RankSpec


class PromotedQueen(Queen):
  _base_rank: Optional[str]

  def __init__(self, spec: RankSpec):
    super().__init__(spec=spec)
    _base_rank = spec.name


  @property
  def base_rank(self) -> Optional[str]:
    return self._base_rank