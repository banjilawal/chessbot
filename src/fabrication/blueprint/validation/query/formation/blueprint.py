# src/blueprint/validation/formation/blueprint.py

"""
Module: blueprint.validation.query.formation.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import FormationNullException
from model import Formation, Blueprint, Game, Player


@dataclass
class FormationQueryValidationBlueprint(QueryValidationBlueprint[Formation]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = FormationNullException()
    model_type = FormationValidation
