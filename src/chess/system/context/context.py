# src/chess/system/context/map.py

"""
Module: chess.system.context.map
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class Context(ABC, Generic[T]):
    """
    # ROLE: Filtering Options, Data Transfer
  
    # RESPONSIBILITIES:
    1.  Provide a set of attribute-value pairs. Used in searches or forward lookups.
    2.  For a search the attribute routes to search-by-attribute method and the value is the search target.
    3.  In a forward hashmap lookup The context represents a SuperKey for a SuperKeyHash{SuperKey: {str: [attribute-value-set]}
  
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
        *   id (Optional[int])
        *   name (Optional[str])
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
        """
        # ACTION:
        1.  Convert a Context into a dictionary.
        2.  Subclasses must implement this method.

        # PARAMETERS:
        None

        # Returns:
            dict

        # RAISES:
        None
        """
        pass