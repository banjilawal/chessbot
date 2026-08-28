# src/domain/metadata/blueprint/context/hostage/blueprint.py

"""
Module: domain.metadata.blueprint.context.hostage.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import HostageStackContextNullException
from domain.model import HostageContext, Blueprint, Game, Player


@dataclass
class HostageContextBlueprint(Blueprint[HostageContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    domain_null_exception = HostageStackContextNullException()
    model_type = HostageContext
