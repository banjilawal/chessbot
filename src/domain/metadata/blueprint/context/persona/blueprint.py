# src/domain/metadata/blueprint/context/persona/blueprint.py

"""
Module: domain.metadata.blueprint.context.persona.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PersonaStackContextNullException
from domain.model import PersonaContext, Blueprint


@dataclass
class PersonaContextBlueprint(Blueprint[PersonaContext]):
    name: Optional[str]
    quota: Optional[int]
    ransom: Optional[int]
    designation: Optional[str]
    null_exception = PersonaStackContextNullException()
    model_type = PersonaContext
