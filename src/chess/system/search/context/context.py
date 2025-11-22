# src/chess/system/search/context/context.py

"""
Module: chess.system.search.context.context
Author: Banji Lawal
Created: 2025-09-28
"""

from typing import Optional
from abc import ABC, abstractmethod


from chess.system import Context, SearchContext


class SearchContext(ABC, Context):
    """
    # ROLE: Option Menu, Switch

    # RESPONSIBILITIES:
    1. Select a mutually exclusive attribute to search by.

    # PROVIDES:
    1. Search options.

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
    """
    _id: Optional[int]
    _name: Optional[str]
    
    
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None):
        self._id = id
        self._name = name
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @classmethod
    def id_context(cls, id: int) -> SearchContext:
        return cls(id=id)
    
    @classmethod
    def name_context(cls, name: str) -> SearchContext:
        return cls(name=name)
    

