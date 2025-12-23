# src/chess/system/find/finder/finder.py

"""
Module: chess.system.find.finder.finder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import abstractmethod
from typing import TypeVar, List

from chess.system import Context, Finder, Validator, SearchResult

T = TypeVar("T")


class DataFinder(Finder[T]):
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
      * _attribute (data_type): <sentence_if_necessary>
    ]
    """
    """
    implement by entities "owning" relationships for unified old_search
    by dataset attributes with validated params.

    Attributes:
      None Implementors declare their own
    """
    
    @classmethod
    @abstractmethod
    def find(
            cls,
            dataset: List[T],
            context: Context[T],
            context_validator: Validator[Context[T]]
    ) -> SearchResult[List[T]]:
        """
        Action:
        Parameters:
            * dataset (List[D])
            * context (Context[D)
            * context_validator (Validator[Context[D])
        Returns:
            SearchResult[List[R]] or Void
        Raise:
          No exception. Subclasses raise exception.
        """
        pass