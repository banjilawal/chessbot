# src/domain/metadata/blueprint/validation/player/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PlayerNullException
from domain.model import Player, Blueprint, Game, Team


@dataclass
class PlayerQueryValidationBlueprint(QueryValidationBlueprint[Player]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a PlayerValidation instance.

    Attributes:
        id: Optional[id]
        name: Optional[str]
        team: Optional[Team]
        game: Optional[Game]
        class_name: Optional[str]
        domain_null_exception = PlayerNullException
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
    domain_null_exception = PlayerNullException()
    model_type = PlayerValidation
