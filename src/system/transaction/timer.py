class CountdownTimer:
  _count_down_start: int

  def __init__(self, count_down_start: int=1000):
    self._count_down_start = count_down_start

  @property
  def count_down_start(self) -> int:
    return self._count_down_start

