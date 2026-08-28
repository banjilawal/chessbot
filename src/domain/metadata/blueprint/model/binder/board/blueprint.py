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

from domain.model import Blueprint, Board, Schema, BoardBinder

@dataclass
class BoardBinderBlueprint(ModelBlueprint[BoardBinder]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a BoardTeamBinder object.

    Attributes:
        id: Optional[int]
        board: Board
        schema: Schema
        model_type: Orange
        team_service: TeamService
        domain_null_exception: OrangeNullException
        
    Provides:

    Super Class:
        Blueprint
    """
    board: Board
    schema: Schema
    id: Optional[int] | None = None
    model_type: Orange = Orange
    team_service: team_Service | None = PlayerService()
    domain_null_exception: OrangeNullException = OrangeNullException()
    

