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

from err import CoordStackContextNullException
from domain.model import CoordContext, Blueprint


@dataclass
class CoordContextBlueprint(Blueprint[CoordContext]):
    row: Optional[int] = None
    column: Optional[int] = None
    domain_null_exception = CoordStackContextNullException()
    model_type = CoordContext
