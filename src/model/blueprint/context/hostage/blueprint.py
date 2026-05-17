# src/model/blueprint/context/hostage/blueprint.py

"""
Module: model.blueprint.context.hostage.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import HostageContextNullException
from model import HostageContext, Blueprint, Game, Player


@dataclass
class HostageContextBlueprint(Blueprint[HostageContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = HostageContextNullException()
    model_type = HostageContext
