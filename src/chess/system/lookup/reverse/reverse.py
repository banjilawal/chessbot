# src/chess/system/lookup/forward/lookup.py

"""
Module: chess.system.lookup.forward.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, List
from typing_extensions import TypeVar

from chess.system import Builder, LoggingLevelRouter, Context, SearchResult, Validator, id_emitter

M = TypeVar("M", bound=Enum)
C = TypeVar("C", bound=Context)


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
    def lookup(cls, context: Context[Enum], context_validator: Validator[Context[Enum]]) -> SearchResult[List[Enum]]:
        """"""
        pass