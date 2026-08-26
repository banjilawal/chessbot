# src/assurance/bundle/structure/node/vector/bundle.py

"""
Module: assurance.bundle.structure.node.vector.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NodeValidationBundle
from domain import VectorNode, VectorNodeTypeUnions, VectorNullExceptionRoster
from transit import VectorValidator


@dataclass
class VectorNodeValidationBundle(NodeValidationBundle[VectorNode]):
    """
    Role:
        -  Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities VectorNodeIntegrityChecker 
            needs to run safety checks on a validation candidate.

    Attributes:
        types: VectorNodeTypeUnions
        nulls: VectorNullExceptionRoster
        
        vector_validator: VectorValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidationBundle
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