# src/exchange/wrapper/validation/struct/node/wrapper.py

"""
Module: exchange.wrapper.validation.struct.node.wrapper
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
    NodeValidationRequest, NodeValidationResponder, StructValidationResponseWrapper,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class NodeValidationResponseWrapper(
    StructValidationResponseWrapper[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Node
                _   The Blueprint
            from a NodeValidationResponse.

    Attributes:
        responder: NodeValidationResponder[T]
        
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
        ValidationResponseWrapper
    """
    
    def __init__(self, responder: NodeValidationResponder[T]):
        """
        Args:
            responder: NodeValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> NodeValidationResponder[T]:
        return cast(NodeValidationResponder[T], super().responder)
    
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