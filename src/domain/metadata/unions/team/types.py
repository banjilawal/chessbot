# src/domain/metadata/unions/team/manifest.py

"""
Module: domain.metadata.unions.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Team, TeamBlueprint
from transit import TeamCarrier


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
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Team] = Team
    carrier: Type[TeamCarrier] = TeamCarrier
    blueprint: Type[TeamBlueprint] = TeamBlueprint