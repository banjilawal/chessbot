# src/blueprint/validation/player/blueprint.py

"""
Module: blueprint.validation.query.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PlayerNullException
from model import Player, Blueprint, Game, Team


@dataclass
class PlayerQueryValidationBlueprint(QueryValidationBlueprint[Player]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a PlayerValidation instance.

    Attributes:
        id: Optional[id]
        name: Optional[str]
        team: Optional[Team]
        game: Optional[Game]
        class_name: Optional[str]
        null_exception = PlayerNullException
        model_type = PlayerValidation

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    id: Optional[id] = None
    name: Optional[str] = None
    team: Optional[Team] = None
    game: Optional[Game] = None
    class_name: Optional[str] = None
    null_exception = PlayerNullException()
    model_type = PlayerValidation
