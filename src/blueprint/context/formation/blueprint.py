# src/blueprint/context/formation/blueprint.py

"""
Module: blueprint.context.formation.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import FormationContextNullException
from model import FormationContext, Blueprint, Game, Player


@dataclass
class FormationContextBlueprint(Blueprint[FormationContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = FormationContextNullException()
    model_type = FormationContext
