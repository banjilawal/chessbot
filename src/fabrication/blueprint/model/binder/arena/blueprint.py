# src/blueprint/model/binder/blueprint.py

"""
Module: blueprint.model.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from microservice import PlayerService
from model import Blueprint, Arena, Schema, ArenaBinder

@dataclass
class ArenaBinderBlueprint(ModelBlueprint[ArenaBinder]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating an ArenaBinderBlueprint object.

    Attributes:
        id: Optional[int]
        arena: Arena
        schema: Schema
        player_service: PlayerService
        null_exception: AreaBinderNullException
        model_type: AreaBinder
        
    Provides:

    Super Class:
        Blueprint
    """
    arena: Arena
    schema: Schema
    id: Optional[int] | None = None
    player_service: PlayerService | None = PlayerService()
    null_exception: AreaBinderNullException = AreaBinderNullException()
    model_type: AreaBinder = AreaBinder
    

