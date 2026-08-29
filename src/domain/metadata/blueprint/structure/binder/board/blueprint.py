# src/domain/metadata/blueprint/structure/binder/blueprint.py

"""
Module: domain.metadata.blueprint.structure.binder.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional

from domain import BoardTeamColorBinder, StructureBlueprint


class BoardBinderBlueprint(StructureBlueprint[BoardTeamColorBinder]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a BoardTeamColorBinder object.

    Attributes:
        board: Board
        schema: Schema
        model_type: Orange
        team_service: TeamService
        domain_null_exception: OrangeNullException
        
    Provides:

    Super Class:
       StructureBlueprint
    """
    board: Board
    schema: Schema
    id: Optional[int] | None = None
    model_type: Orange = Orange
    team_service: team_Service | None = PlayerService()
    domain_null_exception: OrangeNullException = OrangeNullException()
    

