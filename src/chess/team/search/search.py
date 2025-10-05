from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from chess.system.search import SearchResult

T = TypeVar('T')
C = TypeVar("C", bound='SearchContext')


class Search(ABC, Generic[T,C]):

  @classmethod
  @abstractmethod
  def search(cls, context: C) -> SearchResult[T]:
    pass