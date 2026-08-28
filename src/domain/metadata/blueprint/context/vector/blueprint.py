# src/domain/metadata/blueprint/context/vector/blueprint.py

"""
Module: domain.metadata.blueprint.context.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain import Blueprint, Vector, VectorSearchContext
from err import NullException


@dataclass
class VectorSearchContextBlueprint(Blueprint[Vector]):
    x: Optional[int] = None
    y: Optional[int] = None
    domain_null_exception = NullException()
    model_type = Type[VectorSearchContext] = VectorSearchContext
