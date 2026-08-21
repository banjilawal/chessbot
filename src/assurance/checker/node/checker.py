# src/assurance/checker/node/checker.py

"""
Module: assurance.checker.node.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, cast

from assurance import IntegrityChecker, NodeValidationBundle
from domain.node import Node
from result import ValidationResult
from util import LoggingLevelRouter


class NodeIntegrityChecker(IntegrityChecker[Node]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Node instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: NodeValidatorBundle

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: NodeValidationBundle):
        """
        Args:
            bundle: NodeValidatorBundle
        """
        super().__init__(bundle=bundle)
    
    @property
    def bundle(self) -> NodeValidationBundle:
        return cast(NodeValidationBundle, super().bundle)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        pass
    
    
        
        
