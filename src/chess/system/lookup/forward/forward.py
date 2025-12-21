# src/chess/system/lookup/forward/lookup.py

"""
Module: chess.system.lookup.forward.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum
from typing import Generic, List
from typing_extensions import TypeVar
from abc import ABC, abstractmethod


from chess.system import LoggingLevelRouter, Context, SearchResult, Validator


class ForwardLookup(ABC, Generic[Context[Enum]]):
    """
    # ROLE: Table lookup, Finder

    # RESPONSIBILITIES:
    1.  Find metadata based on attribute values.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
 

    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def lookup(cls, super_key: Context[Enum], super_key_validator: Validator[Context[Enum]]) -> SearchResult[List[Enum]]:
        """"""
        pass
    
    