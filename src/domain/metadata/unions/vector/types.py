# src/domain/metadata/unions/arena/manifest.py

"""
Module: domain.metadata.unions.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Arena, ArenaBlueprint, TypeUnion
from transit import ArenaCarrier


@dataclass
class ArenaTypeUnion(TypeUnion[Arena]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Arena uses in the domain.

    Attributes:
        model: Type[Arena] = Arena
        carrier: Type[ArenaCarrier] = ArenaCarrier
        blueprint: Type[ArenaBlueprint] = ArenaBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Arena] = Arena
    carrier: Type[ArenaCarrier] = ArenaCarrier
    blueprint: Type[ArenaBlueprint] = ArenaBlueprint