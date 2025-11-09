# src/chess/system/search/search.py

"""
Module: `chess.system.search.search`
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

from chess.system.search import SearchContext, SearchResult

A = TypeVar('A')
S = TypeVar('S', bound=SearchContext)
R = TypeVar('R')

class Search(ABC, Generic[A, S, R]):
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  [
    <No attributes. Implementors declare their own.>
  OR
    * `_attribute` (`data_type`): <sentence_if_necessary>
  ]
  """
  """
  implement by entities "owning" relationships for unified old_search
  by collection attributes with validated params.

  Attributes:
    No attributes. Implementors declare their own
  """

  @classmethod
  @abstractmethod
  def search(cls, data_owner: A, search_context: S, *args, **kwargs) -> SearchResult[R]:
      pass
      """
      Action:
      Parameters:
          * `data_owner` (`A`):
          * `search_context` (`S`):
      Returns:
          `SearchResult[List[R]]` or `Void`
      Raise:
        No exceptions. Subclasses raise exceptions.
      """
