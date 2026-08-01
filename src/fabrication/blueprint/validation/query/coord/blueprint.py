# src/blueprint/validation/coord/blueprint.py

"""
Module: blueprint.validation.query.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import CoordNullException
from model import Coord, Blueprint, Game, Player


@dataclass
class CoordQueryValidationBlueprint(QueryValidationBlueprint[Coord]):
    row: Optional[int] = None
    column: Optional[int] = None
    null_exception = CoordNullException()
    model_type = CoordValidation
