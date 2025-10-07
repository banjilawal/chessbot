# chess/system/search/roster.py

"""
Module: `chess.system.search.search`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: AWT implement by entities "owning" relationships for unified
  search by collection attributes with validated params.

Contains:
 * `Search`
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from chess.system import SearchContext, FilterContext, SearchResult, FilterResult

T = TypeVar('T')

class Search(ABC, Generic[T]):
  """
  implement by entities "owning" relationships for unified search
  by collection attributes with validated params.

  Attributes:
    No attributes. Implementors declare their own
  """

  @classmethod
  @abstractmethod
  def search(cls, search_context: SearchContext, *args, **kwargs) -> SearchResult[T]:
    """
    Validates provided filter. Returns first match.
    Args:
    - `collection_master` (`M`): The data owning entity.
    - `data_set` (`D`): The data collection searched.
    - `filter` (`F`): The search filter to hit,
    - `search_context` (`C`): List of data set attributes.
    Returns:
      `SearchResult[`T`]`

    Raise:
      No exceptions. Subclasses raise exceptions.
    """
    pass


  @classmethod
  @abstractmethod
  def filter(cls, filter_context: FilterContext, *args, **kwargs) -> FilterResult[T]:
    pass