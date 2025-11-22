# src/chess/system/search/context/_service.py

"""
Module: chess.system.search.context.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from abc import abstractmethod

from chess.system import BuildResult, Builder, Validator, SearchContext


class SearchContextService:
    _builder: Builder[SearchContext]
    _validator: Validator[SearchContext]
    
    def __init__(
            self,
            builder: Builder[SearchContext],
            validator: Validator[SearchContext]
    ):
        self._builder = builder
        self._validator = validator
        
    @property
    def validator(self) -> Validator[SearchContext]:
        return self._validator
    
    @abstractmethod
    def build(
            self,
            context_validator: Validator[SearchContext],
            *args,
            **kwargs
    ) -> BuildResult[SearchContext]:
        pass