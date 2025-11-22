# src/chess/system/search/context/context.py

"""
Module: chess.system.search.context.context
Author: Banji Lawal
Created: 2025-09-28
"""

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar



from chess.system import Context, SearchContext

T = TypeVar("T")

class SearchContext(ABC, Context[Generic[T]]):
    """
    # ROLE: Option Menu, Switch

    # RESPONSIBILITIES:
    1.  Provides a series of flags corresponding to an attribute in T. Supplying a
        target value enables a flag.
    2.  Scalable, extensible, and reusable management of different search permutations.
    

    # PROVIDES:
    1. Search options.

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
    """
    _id: Optional[int]
    _name: Optional[str]
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None
    ):
        self._id = id
        self._name = name
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass
    

