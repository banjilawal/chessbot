# src/blueprint/validation/schema/blueprint.py

"""
Module: blueprint.validation.query.schema.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SchemaNullException
from model import Schema, Blueprint
from setting import GameColor


@dataclass
class SchemaQueryValidationBlueprint(QueryValidationBlueprint[Schema]):
    
    name: Optional[str] | None = None
    color: Optional[GameColor] | None = None
    null_exception = SchemaNullException()
    model_type = SchemaValidation
