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
    """
    # ROLE: Service, Encapsulation, API layer.
    
    # RESPONSIBILITIES:
    1.  Provide a single entry point for SearchContextBuilder and SearchContextValidator objects.
    2.  Passing its own validator to the internal builder simplifies the SearchContext lifecycle.
    3.  Protects SearchContext from direct, unprotected access.
    4.  Public facing API.
    
    # PROVIDES:
        *   Direct access tp SearchContextValidator
        *   Interface to SearchContextBuilder
    
    # ATTRIBUTES:
        *   _builder (SearchContextBuilder):
        *   _validator (SearchContextValidator):
    """
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
        """
        Validators may have extra features and logic.
        Direct access is given ta all the Validator's capabilities.
        """
        return self._validator
    
    @abstractmethod
    def build(self, *args, **kwargs) -> BuildResult[SearchContext]:
        """
        Implementations must inject self._validator into
        self._builder along with any other dependencies and params.
        """
        pass