# src/logic/token/database/search/context/service/operation/controller.py

"""
Module: logic.token.database.search.context.service.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from logic.token import TokenBuilder, TokenContextIntegrityWorkers, TokenValidator


class TokenContextOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenService supports.
        
    Attributes:
        builder: TokenBuilder
        validator: TokenValidator
        workers: TokenContextIntegrityWorkers

    Provides:
    
    Super Class:
    """
    _builder: TokenBuilder
    _validator: TokenValidator
    _workers: TokenContextIntegrityWorkers
    
    def __init__(
            self,
            builder: TokenBuilder = TokenBuilder(),
            validator: TokenValidator = TokenValidator(),
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ):
        """
        Args:
            builder: TokenBuilder
            validator: TokenValidator
            workers: TokenContextIntegrityWorkers
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = workers
        
    @property
    def builder(self) -> TokenBuilder:
        return self._builder
        
    @property
    def validator(self) ->TokenValidator:
        return self._validator
    
    @property
    def arithmetic(self) -> TokenContextIntegrityWorkers:
        return self._arithmetic