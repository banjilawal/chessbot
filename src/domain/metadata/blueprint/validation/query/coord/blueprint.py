# src/domain/metadata/blueprint/validation/coord/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import CoordNullException
from domain.model import Coord, Blueprint


@dataclass
class CoordQueryValidationBlueprint(QueryValidationBlueprint[Coord]):
    row: Optional[int] = None
    column: Optional[int] = None
    domain_null_exception = CoordNullException()
    model_type = CoordValidation
