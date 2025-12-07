# src/chess/system/searcher/service.py

"""
Module: chess.system.searcher.searcher
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

from chess.system import Context, Validator, SearchResult

D = TypeVar("D")

class Search(ABC, Generic[D]):
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
  by data_set attributes with validated params.

  Attributes:
    None Implementors declare their own
  """

  @classmethod
  @abstractmethod
  def find(
          cls,
          data_set: List[D],
          context: Context[D],
          context_validator: Validator[Context[D]]
  ) -> SearchResult[List[D]]:
      """
      Action:
      Parameters:
          * data_set (List[D])
          * context (Context[D)
          * context_validator (Validator[Context[D])
      Returns:
          SearchResult[List[R]] or Void
      Raise:
        No exceptions. Subclasses raise exceptions.
      """
      pass

