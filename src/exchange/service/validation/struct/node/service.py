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
    NodeValidationRequest, NodeValidationService, StructValidationService,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class NodeValidationService(
    StructValidationService[T], ABC, Generic[T]
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
        service: NodeValidationService[T]
        
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
    
    def __init__(self, service: NodeValidationService[T]):
        """
        Args:
            service: NodeValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> NodeValidationService[T]:
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