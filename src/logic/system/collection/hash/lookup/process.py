# src/logic/system/collection/hash/lookup/process.py

"""
Module: logic.system.collection.hash.lookup.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum
from typing import List
from abc import abstractmethod

from logic.system import SearchProcess, Context, LoggingLevelRouter, SearchResult, ValidationProcess


class HashLookupProcess(SearchProcess[Enum]):
    """
    Role:Forward Lookups,

    Responsibilities:
    1.  Use Key (metadata_attribute: value) to find entries in
            StrategyContractorHashMap{StrategyTitle: {ContractorBuildMetadata}
    2.  Use Key to find entries in CategoryHashMap{Name: Tuple}
    3.  Indicate the HashMap does have an entry for the Key with an exception in the SearchResult.

    Super Class:
        *   SearchProcess

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def query(
            cls,
            super_key: Context[Enum],
            super_key_validator: ValidationProcess[Context[Enum]]
    ) -> SearchResult[List[Enum]]:
        """"""
        pass

