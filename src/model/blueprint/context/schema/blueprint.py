# src/model/blueprint/context/schema/blueprint.py

"""
Module: model.blueprint.context.schema.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import SchemaContext, Blueprint
from system import GameColor


@dataclass
class SchemaContextBlueprint(Blueprint[SchemaContext]):
    name: Optional[str] = None
    color: Optional[GameColor] = None
