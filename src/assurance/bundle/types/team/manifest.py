# src/assurance/manifest/types/team/manifest.py

"""
Module: assurance.manifest.types.team.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import TeamBlueprint
from domain.model import Team
from transit import TeamCarrier


@dataclass
class TeamTypes(TypesManifest[Team]):
    model: Type[Team] = Team
    carrier: Type[TeamCarrier] = TeamCarrier
    blueprint: Type[TeamBlueprint] = TeamBlueprint