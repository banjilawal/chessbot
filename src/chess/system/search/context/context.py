# src/chess/system/search/context/context.py

"""
Module: chess.system.search.context.context
Author: Banji Lawal
Created: 2025-09-28
"""

from abc import ABC, abstractmethod
from typing import Optional

from chess.system import Context


class SearchContext(ABC, Context):
    """
    # ROLE: Encapsulation

    # RESPONSIBILITIES:
    1. Simplify the number of parameters and their possible combinations passed to a old_search method.

    # PROVIDES:
    1. A dictionary of options and specifications of what the old_search service returns.

    # ATTRIBUTES:
      * See `Context` superclass for attributes.
    """
    _id: Optional[int]
    _name: Optional[str]
    
    
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None):
        self._id = id
        self._name = name
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name




    @classmethod
    @abstractmethod
    def to_dict(self) -> dict:
        pass