# src/domain/metadata/blueprint/validation/schema/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.schema.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import SchemaNullException
from domain.model import Schema, Blueprint
from config.setting import GameColor


@dataclass
class SchemaQueryValidationBlueprint(QueryValidationBlueprint[Schema]):
    
    name: Optional[str] | None = None
    color: Optional[GameColor] | None = None
    domain_null_exception = SchemaNullException()
    model_type = SchemaValidation
