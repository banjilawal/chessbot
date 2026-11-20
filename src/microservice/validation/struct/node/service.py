# src/exchange/service/validation/struct/node/service.py

"""
Module: exchange.service.validation.struct.node.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Node, NodeBlueprint
from exchange import (
    NodeValidationRequest, NodeValidationService, ValidationMicroservice,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class NodeValidationService(
    ValidationMicroservice[T], ABC, Generic[T]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Node
                _   The Blueprint
            from a NodeValidationResponse.

    Attributes:
        dispatcher: NodeValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: NodeValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: NodeValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, dispatcher: NodeValidationService[T]):
        """
        Args:
            dispatcher: NodeValidationService[T]
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> NodeValidationService[T]:
        return cast(NodeValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: NodeValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: NodeValidationRequest[T]
    ) -> ValidationResult[NodeBlueprint[T]]:
        pass