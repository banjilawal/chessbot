# /src/chess/system/search/context.py

"""
Module: `chess.system.search.context`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Responsibilities: Dictionary of datasets and their attributes for searching
  collections owned by an entity.

Contains:
 * `SearchContext`
"""


from abc import ABC

from chess.system import Context


class SearchContext(Context, ABC):
  """
  AWT that `Search` implementors must pass to their `search` method.
  A `SearchContext` lowers the number of parameters a method needs
  while providing order-independent ways of combining search parameters.

  Attributes:
    No attributes. Implementors declare their own.
  """
  pass