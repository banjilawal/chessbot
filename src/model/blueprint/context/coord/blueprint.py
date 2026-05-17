# src/model/blueprint/context/coord/blueprint.py

"""
Module: model.blueprint.context.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import CoordContextNullException
from model import CoordContext, Blueprint, Game, Player


@dataclass
class CoordContextBlueprint(Blueprint[CoordContext]):
    row: Optional[int] = None
    column: Optional[int] = None
    null_exception = CoordContextNullException()
    model_type = CoordContext
