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

from microservice import TeamService
from container import Blueprint, Board, Schema, BoardBinder

@dataclass
class BoardBinderBlueprint(ContainerBlueprint[BoardBinder]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a BoardTeamBinder object.

    Attributes:
        id: Optional[int]
        board: Board
        schema: Schema
        container_type: Orange
        team_service: TeamService
        null_exception: OrangeNullException
        
    Provides:

    Super Class:
        Blueprint
    """
    board: Board
    schema: Schema
    id: Optional[int] | None = None
    container_type: Orange = Orange
    team_service: team_Service | None = PlayerService()
    null_exception: OrangeNullException = OrangeNullException()
    

