# src/domain/metadata/unions/model/searchable/state/team/manifest.py

"""
Module: domain.metadata.unions.model.searchable.state.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Team, TeamBlueprint, TeamCarrier, TeamSearchSearchContext


@dataclass
class TeamTypeUnions(ModelTypeUnions[Team]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Team uses in the domain.

    Attributes:
        model: Type[Team] = Team
        carrier: Type[TeamCarrier] = TeamCarrier
        blueprint: Type[TeamBlueprint] = TeamBlueprint
        search_context: Type[TeamSearchContext] = TeamSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Team] = Team
    carrier: Type[TeamCarrier] = TeamCarrier
    blueprint: Type[TeamBlueprint] = TeamBlueprint
    search_context: Type[TeamSearchSearchContext] = TeamSearchSearchContext