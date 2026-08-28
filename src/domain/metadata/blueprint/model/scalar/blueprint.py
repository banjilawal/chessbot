# src/domain/metadata/blueprint/model/scalar/blueprint.py

"""
Module: domain.metadata.blueprint.model.scalar.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from err import ScalarNullException
from domain.model import Blueprint, Scalar

@dataclass
class ScalarBlueprint(ModelBlueprint[Scalar]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides magnitude value for hydrating a Scalar object.

    Attributes:
        magnitude: int
        model_type: Scalar
        domain_null_exception: ScalarNullException
    Provides:

     Super Class:
        ModelBlueprint
     """
    magnitude: int
    domain_null_exception: ScalarNullException = ScalarNullException()
    owner: Scalar = Type[Scalar]
    owner_name: str = type(owner).__name__
