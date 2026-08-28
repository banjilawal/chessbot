# src/domain/metadata/blueprint/model/binder/blueprint.py

"""
Module: domain.metadata.blueprint.model.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from microservice import PlayerService
from domain.model import Blueprint, Arena, Schema, ArenaBinder

@dataclass
class ArenaBinderBlueprint(ModelBlueprint[ArenaBinder]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating an ArenaBinderBlueprint object.

    Attributes:
        id: Optional[int]
        arena: Arena
        schema: Schema
        player_service: PlayerService
        domain_null_exception: AreaBinderNullException
        model_type: AreaBinder
        
    Provides:

    Super Class:
        Blueprint
    """
    arena: Arena
    schema: Schema
    id: Optional[int] | None = None
    player_service: PlayerService | None = PlayerService()
    domain_null_exception: AreaBinderNullException = AreaBinderNullException()
    model_type: AreaBinder = AreaBinder
    

