# src/chess/system/context/base.py

"""
Module: chess.system.context.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class Context(ABC, Generic[T]):
    """
    # ROLE: Option Selection,
  
    # RESPONSIBILITIES:
    1.  Provides a series key-value pairs for selecting which operation should be performed with what attribute
        value.
    2.  Provide a single entry point into different logic flows in an easy, scalable manner.
    3.  Utility for factories.
  
  
    # PROVIDES:
    1. Search options.
  
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