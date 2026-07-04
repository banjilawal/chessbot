# src/logic/token/database/search/context/service/operation/controller.py

"""
Module: logic.token.database.search.context.service.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from model.state.token import TokenContextBuilder, TokenContextIntegrityWorkers, TokenContextValidator


class TokenContextOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenService supports.
        
    Attributes:
        builder: TokenContextBuilder
        validator: TokenContextValidator
        workers: TokenContextIntegrityWorkers

    Provides:
    
    Super Class:
    """
    _builder: TokenContextBuilder
    _validator: TokenContextValidator
    _workers: TokenContextIntegrityWorkers
    
    def __init__(
            self,
            builder: TokenContextBuilder = TokenContextBuilder(),
            validator: TokenContextValidator = TokenContextValidator(),
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ):
        """
        Args:
            builder: TokenContextBuilder
            validator: TokenContextValidator
            workers: TokenContextIntegrityWorkers
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = workers
        
    @property
    def builder(self) -> TokenContextBuilder:
        return self._builder
        
    @property
    def validator(self) ->TokenContextValidator:
        return self._validator
    
    @property
    def arithmetic(self) -> TokenContextIntegrityWorkers:
        return self._arithmetic