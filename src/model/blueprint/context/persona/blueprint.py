# src/model/blueprint/context/persona/blueprint.py

"""
Module: model.blueprint.context.persona.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PersonaContextNullException
from model import PersonaContext, Blueprint, Game, Player


@dataclass
class PersonaContextBlueprint(Blueprint[PersonaContext]):
    name: Optional[str]
    quota: Optional[int]
    ransom: Optional[int]
    designation: Optional[str]
    null_exception = PersonaContextNullException()
    model_type = PersonaContext
