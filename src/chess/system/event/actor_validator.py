from abc import ABC
from typing import TypeVar, Generic

from chess.system import ValidationResult

A = TypeVar('A')
X = TypeVar('X')
T = TypeVar('T')

class ActorValidator(ABC, Generic[A, X, T]):
  """"""

  @classmethod
  def validate(cls, actor: A, execution_environment: X) -> ValidationResult[T]:
      pass
