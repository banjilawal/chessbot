# src/domain/metadata/blueprint/validation/persona/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.persona.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PersonaNullException
from domain.model import Persona, Blueprint


@dataclass
class PersonaQueryValidationBlueprint(QueryValidationBlueprint[Persona]):
    name: Optional[str]
    quota: Optional[int]
    ransom: Optional[int]
    designation: Optional[str]
    null_exception = PersonaNullException()
    model_type = PersonaValidation
