# src/assurance/toolkit/structure/node/vector/toolkit.py

"""
Module: assurance.toolkit.structure.node.vector.toolkit
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NodeValidatorToolkit
from domain import VectorNode, VectorNodeTypeUnions, VectorNullExceptionRoster
from transit import VectorValidator


@dataclass
class VectorNodeValidatorToolkit(NodeValidatorToolkit[VectorNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Toolkits types, null-exceptions, attribute-validators, and utilities VectorNodeIntegrityChecker 
            needs to run safety checks on a validation candidate.

    Attributes:
        types: VectorNodeTypeUnions
        nulls: VectorNullExceptionRoster
        
        vector_validator: VectorValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidatorToolkit
    """
    types: VectorNodeTypeUnions = VectorNodeTypeUnions()
    nulls: VectorNullExceptionRoster = VectorNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "vector_validator": VectorValidator(),
        }
    )

    @property
    def vector_validator(self) -> VectorValidator:
        return self.resources["vector_validator"]