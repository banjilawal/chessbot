# src/transit/dispatcher/validator/structure/node/validator.py

"""
Module: transit.dispatcher.validator.node.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, cast

from assurance import NodeValidator, Validator
from domain.structure.node import Node
from artifcat import ValidationResult
from util import LoggingLevelRouter


class NodeValidator(Validator[Node]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Node instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: NodeValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, validator: NodeValidator):
        """
        Args:
            validator: NodeValidator
        """
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> NodeValidator:
        return cast(NodeValidator, super().validator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
