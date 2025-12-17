# src/chess/system/metadata/lookup/lookup.py

"""
Module: chess.system.metadata.lookup.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from abc import ABC, abstractmethod
from typing import Generic
from typing_extensions import TypeVar

from chess.system import Builder, LoggingLevelRouter, Metadata, Context, SearchResult, Validator

M = TypeVar("M", bound=Metadata)
C = TypeVar("C", bound=Context)


class MetadataLookup(ABC, Generic[Context[M]]):
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
    _context_builder: Builder[Context[Metadata]]
    _context_validator: Validator[Context[Metadata]]
    _metadata_validator: Validator[Metadata]
    
    def __init__(
            self,
            context_builder: Builder[Context[Metadata]],
            context_validator: Validator[Context[Metadata]],
            metadata_validator: Validator[Metadata],
    ):
        self._context_builder = context_builder
        self._context_validator = context_validator
        self._metadata_validator = metadata_validator
    
    
    @property
    def metadata_validator(self) -> Validator[Metadata]:
        return self._metadata_validator
    
    @property
    def context_builder(self) -> Builder[Context[Metadata]]:
        return self._context_builder
    
    @property
    def context_validator(self) -> Validator[Context[Metadata]]:
        return self._context_validator

    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def lookup(cls, context: Context[Metadata]) -> SearchResult[Metadata]:
        pass
    
    