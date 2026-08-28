# src/domain/metadata/blueprint/context/coord/blueprint.py

"""
Module: domain.metadata.blueprint.context.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from domain import Blueprint, CoordSearchContext
from err import CoordSearchContextNullException



@dataclass
class CoordSearchContextBlueprint(Blueprint[CoordSearchContext]):
    row: Optional[int] = None
    column: Optional[int] = None
    domain_null_exception = CoordSearchContextNullException()
    model_type = CoordSearchContext
