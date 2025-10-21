from typing import  TYPE_CHECKING


from chess.commander import  Commander


class Human(Commander):

  def __init__(self, id: int,  name: str):
    super().__init__(id, name)

  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, Human):
        return True
    return False

  def __hash__(self):
    return hash(self.id)