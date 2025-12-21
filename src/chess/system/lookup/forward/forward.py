# src/chess/system/lookup/forward/lookup.py

"""
Module: chess.system.lookup.forward.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum
from typing import Generic, List
from abc import ABC, abstractmethod


from chess.system import LoggingLevelRouter, Context, SearchResult, Validator


class ForwardLookup(ABC, Generic[Context[Enum]]):
    """
    # ROLE: Forward Lookups,

    # RESPONSIBILITIES:
    1.  Use SuperKey (metadata_attribute: value) to find entries in
            StrategyContractorHashMap{StrategyTitle: {ContractorBuildMetadata}
    2.  Use SuperKey to find entries in CategoryHashMap{Name: Tuple}
    3.  Indicate the HashMap does have an entry for the SuperKey with an exception in the SearchResult.

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
    def forward_lookup(
            cls,
            super_key: Context[Enum],
            super_key_validator: Validator[Context[Enum]],
    ) -> SearchResult[List[Enum]]:
        """"""
        pass
    
    