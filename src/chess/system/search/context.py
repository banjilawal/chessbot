# /src/chess/system/search/context.py

"""
Module: `chess.system.search.context`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Responsibilities: Dictionary of datasets and their attributes for searching
    a relationship owner's collections.

Contains:
 * `SearchContext`
"""


from abc import ABC

from chess.system import Context


class SearchContext(Context, ABC):
    """
    AWT that `Search` implementors must pass to their `search` method..

    Attributes:
        No attributes. Implementors declare their own.>
    """
    pass