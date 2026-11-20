# src/exchange/service/validation/context/service.py

"""
Module: exchange.service.validation.context.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Context
from exchange import  ContextValidationDispatcher, ValidationService

T = TypeVar("T", bound="Context")

class ContextValidationService(ValidationService[T], ABC, Generic[T]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Context
                _   The Blueprint
            from a ContextValidationResponsder.

    Attributes:
        dispatcher: ContextValidationDispatcher[T]
        
    Provides:
        -   def extract_model(
                    request: ContextValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    request: ContextValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, dispatcher: ContextValidationDispatcher[T]):
        """
        Args:
            dispatcher: ContextValidationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)