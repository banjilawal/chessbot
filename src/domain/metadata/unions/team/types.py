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

from domain import Team, TeamBlueprint, TypeUnion
from transit import TeamCarrier


@dataclass
class TeamTypeUnion(TypeUnion[Team]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Team uses in the domain.

    Attributes:
        model: Type[Team] = Team
        carrier: Type[TeamCarrier] = TeamCarrier
        blueprint: Type[TeamBlueprint] = TeamBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Team] = Team
    carrier: Type[TeamCarrier] = TeamCarrier
    blueprint: Type[TeamBlueprint] = TeamBlueprint