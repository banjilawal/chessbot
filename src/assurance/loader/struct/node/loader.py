# src/assurance/load/struct/node/loader.py

"""
Module: assurance.load.struct.node.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import NodeValidatorToolkit, StructLoader
from domain import Node, NodePrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Node")

class NodeLoader(StructLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   NodeValidationRequest[T]
            -   NodeCarrier[T]
            -   NodeBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[NodePrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: NodeValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> NodeValidatorToolkit[T]:
        return cast(NodeValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[NodePrimeExtract[T]]:
        """
        Extract a safe NodeBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[NodeBlueprint[T]]
        Raises:
            NodeExtractorException
        """
        pass