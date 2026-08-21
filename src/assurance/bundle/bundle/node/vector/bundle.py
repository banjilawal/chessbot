# src/assurance/manifest/bundle/manifest.py

"""
Module: assurance.manifest.bundle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NodeValidationBundle, VectorNodeNullRoster, VectorNodeTypes, VectorValidator


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