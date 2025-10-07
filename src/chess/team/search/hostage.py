from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from chess.system.search import SearchResult


T = TypeVar('T')
C = TypeVar("C", bound='SearchContext')


class TeamRosterSearch(Search):

  @classmethod
  @abstractmethod
  def search(cls, team: Team, context: RosterSearchContext) -> SearchResult[Piece]:
    if context.piece_id not None:
