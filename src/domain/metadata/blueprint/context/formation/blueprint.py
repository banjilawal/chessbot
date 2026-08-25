# src/domain/metadata/blueprint/context/formation/blueprint.py

"""
Module: domain.metadata.blueprint.context.formation.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import FormationStackContextNullException
from domain.model import FormationContext, Blueprint, Game, Player


@dataclass
class FormationContextBlueprint(Blueprint[FormationContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = FormationStackContextNullException()
    model_type = FormationContext
