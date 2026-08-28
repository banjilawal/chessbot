# src/domain/metadata/blueprint/validation/hostage/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.hostage.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import HostageNullException
from domain.model import Hostage, Blueprint, Game, Player


@dataclass
class HostageQueryValidationBlueprint(QueryValidationBlueprint[Hostage]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    domain_null_exception = HostageNullException()
    model_type = HostageValidation
