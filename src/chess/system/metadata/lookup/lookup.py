# src/chess/system/metadata/lookup/lookup.py

"""
Module: chess.system.metadata.lookup.lookup
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
    _id: int
    _name: str
    _enum_validator: Validator[Enum]
    _context_builder: Builder[Context[Enum]]
    _context_validator: Validator[Context[Enum]]
    
    def __init__(
            self,
            id: int,
            name: str,
            enum_validator: Validator[Enum],
            context_builder: Builder[Context[Enum]],
            context_validator: Validator[Context[Enum]],
    ):
        self._id = id
        self._name = name
        self._enum_validator = enum_validator
        self._context_builder = context_builder
        self._context_validator = context_validator

    @property
    def id(self) -> int:
        return self._id
    
    @@property
    def name(self) -> str:
        return self._name
    
    @property
    def enum_validator(self) -> Validator[Enum]:
        return self._enum_validator
    
    @property
    def context_builder(self) -> Builder[Context[Enum]]:
        return self._context_builder
    
    @property
    def context_validator(self) -> Validator[Context[Enum]]:
        return self._context_validator

    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def lookup(cls, context: Context[Enum], context_validator: Validator[Context[Enum]]) -> SearchResult[List[Enum]]:
        pass
    
    