# src/logic/token/database/search/context/service/operation/controller.py

"""
Module: logic.token.database.search.context.service.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from model.token import TokenQueryBuilder, TokenContextIntegrityWorkers, TokenQueryValidator


class TokenQueryOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenService supports.
        
    Attributes:
        builder: TokenQueryBuilder
        validator: TokenQueryValidator
        workers: TokenContextIntegrityWorkers

    Provides:
    
    Super Class:
    """
    _builder: TokenQueryBuilder
    _validator: TokenQueryValidator
    _workers: TokenContextIntegrityWorkers
    
    def __init__(
            self,
            builder: TokenQueryBuilder = TokenQueryBuilder(),
            validator: TokenQueryValidator = TokenQueryValidator(),
            workers: TokenContextIntegrityWorkers = TokenContextIntegrityWorkers(),
    ):
        """
        Args:
            builder: TokenQueryBuilder
            validator: TokenQueryValidator
            workers: TokenContextIntegrityWorkers
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = workers
        
    @property
    def builder(self) -> TokenQueryBuilder:
        return self._builder
        
    @property
    def validator(self) ->TokenQueryValidator:
        return self._validator
    
    @property
    def arithmetic(self) -> TokenContextIntegrityWorkers:
        return self._arithmetic