# src/domain/metadata/blueprint/context/schema/blueprint.py

"""
Module: domain.metadata.blueprint.context.schema.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SchemaContextNullException
from domain.model import SchemaContext, Blueprint
from config.setting import GameColor


@dataclass
class SchemaContextBlueprint(Blueprint[SchemaContext]):
    
    name: Optional[str] | None = None
    color: Optional[GameColor] | None = None
    null_exception = SchemaContextNullException()
    model_type = SchemaContext
