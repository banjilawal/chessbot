# src/chess/system/hash/lookup.py

"""
Module: chess.system.hash.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum
from typing import List
from abc import abstractmethod

from chess.system import Context, Finder, LoggingLevelRouter, SearchResult, Validator


class HashLookup(Finder[Enum]):
    """
    # ROLE: Forward Lookups,

    # RESPONSIBILITIES:
    1.  Use Key (metadata_attribute: value) to find entries in
            StrategyContractorHashMap{StrategyTitle: {ContractorBuildMetadata}
    2.  Use Key to find entries in CategoryHashMap{Name: Tuple}
    3.  Indicate the HashMap does have an entry for the Key with an exception in the SearchResult.

    # PARENT:
        *   Finder

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
    def query(cls, super_key: Context[Enum], super_key_validator: Validator[Context[Enum]]) -> SearchResult[List[Enum]]:
        """"""
        pass

