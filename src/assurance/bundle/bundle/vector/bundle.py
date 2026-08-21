# src/assurance/manifest/bundle/vector/bundle.py

"""
Module: assurance.manifest.bundle.vector.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle, VectorNullRoster, VectorTypes
from domain.model import Vector


@dataclass
class VectorValidationBundle(ValidationBundle[Vector]):
    types: VectorTypes = VectorTypes()
    nulls: VectorNullRoster = VectorNullRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "number_validator": NumberValidator(),
        }
    )
    
    @property
    def number_validator(self) -> NumberValidator:
        return self.resources["number_validator"]
