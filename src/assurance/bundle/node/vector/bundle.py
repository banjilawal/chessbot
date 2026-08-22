# src/assurance/bundle/node/vector/bundle.py

"""
Module: assurance.bundle.node.vector.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NodeValidationBundle, VectorValidator
from domain import VectorNodeNullRoster, VectorNodeTypes


@dataclass
class VectorNodeValidationBundle(NodeValidationBundle):
    types: VectorNodeTypes
    nulls: VectorNodeNullRoster
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "vector_validator": VectorValidator(),
        }
    )

    @property
    def vector_validator(self) -> VectorValidator:
        return self.resources["vector_validator"]