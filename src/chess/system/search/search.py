# chess/system/search/search.py

"""
Module: `chess.system.search.search`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Responsibilities: AWT implement by entities "owning" relationships for unified
    search by collection attributes with validated params.

Contains:
 * `Search`
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from chess.system.search import SearchResult


M = TypeVar('M')
D = TypeVar('D')
F = TypeVar('F')
T = TypeVar('T')
C = TypeVar("C", bound='SearchContext')


class Search(ABC, Generic[M, D, F, T,C]):
    """
    implement by entities "owning" relationships for unified search
    by collection attributes with validated params.

    Attributes:
        No attributes. Implementors declare their own
    """

    @classmethod
    @abstractmethod
    def search(cls, collection_master: M, data_set: D, filter: F, context: C) -> SearchResult['T']:
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