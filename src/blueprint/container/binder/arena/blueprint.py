# src/blueprint/container/binder/blueprint.py

"""
Module: blueprint.container.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from microservice import PlayerService
from container import Blueprint, Arena, Schema, ArenaBinder

@dataclass
class ArenaBinderBlueprint(ContainerBlueprint[ArenaBinder]):
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
        container_type: AreaBinder
        
    Provides:

    Super Class:
        Blueprint
    """
    arena: Arena
    schema: Schema
    id: Optional[int] | None = None
    player_service: PlayerService | None = PlayerService()
    null_exception: AreaBinderNullException = AreaBinderNullException()
    container_type: AreaBinder = AreaBinder
    

