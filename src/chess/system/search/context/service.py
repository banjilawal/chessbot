# src/chess/system/search/context/_security_service.py

"""
Module: chess.system.search.context.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import BuildResult, Builder, Validator, SearchContext

# A = TypeVar("A")
# C = TypeVar("C", biding="SearchContext[C]")
T = TypeVar("T")


class SearchContextService(Generic[T]):
    """
    # ROLE: IntegrityService, Encapsulation, API layer.
    
    # RESPONSIBILITIES:
    1.  Provide a single entry point for SearchContextBuilder and SearchContextValidator objects.
    2.  Passing its own validator to the internal builder simplifies the SearchContext lifecycle.
    3.  Protects SearchContext from direct, unprotected access.
    4.  Public facing API.
    
    # PROVIDES:
        *   Direct access tp SearchContextValidator
        *   Interface to SearchContextBuilder
    
    # ATTRIBUTES:
        *   _item_builder (SearchContextBuilder):
        *   _item_validator (SearchContextValidator):
    """
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(
            self,
            builder: Builder[T],
            validator: Validator[T]
    ):
        self._builder = builder
        self._validator = validator
        
    @property
    def validator(self) -> Validator[T]:
        return self._validator
    
    @property
    def builder(self) -> Builder[T]:
        return self._builder
    
    # @abstractmethod
    # def build(self, *args, **kwargs) -> BuildResult[C]:
    #     """
    #     Implementations must inject self._item_validator into
    #     self._item_builder along with any other dependencies and params.
    #     """
    #     pass