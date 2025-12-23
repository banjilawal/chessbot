# src/chess/system/lookup/reverse/lookup.py

"""
Module: chess.system.lookup.reverse.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum
from typing import Generic, List, TypeVar
from abc import abstractmethod

from chess.system import LoggingLevelRouter, SearchResult, Validator
from chess.system.lookup.lookup import Lookup

T = TypeVar("T")

class ReverseLookup(Lookup[Generic[T]]):
    """
    # ROLE: Reverse Lookups,

    # RESPONSIBILITIES:
    1.  Find a class from an Enum that implements either
        *   StrategyContractorHashMap{StrategyTitle: {ContractorBuildMetadata}
        *   CategoryHashMap{Name: Tuple}

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
    def reverse_lookup(cls, member: Enum, enum_validator: Validator[Enum],) -> SearchResult[List[T]]:
        """"""
        pass