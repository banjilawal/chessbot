# src/domain/metadata/unions/path/manifest.py

"""
Module: domain.metadata.unions.path.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Path, PathBlueprint, TypeUnion
from transit import PathCarrier


@dataclass
class PathTypeUnion(TypeUnion[Path]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Path uses in the domain.

    Attributes:
        model: Type[Path] = Path
        carrier: Type[PathCarrier] = PathCarrier
        blueprint: Type[PathBlueprint] = PathBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Path] = Path
    carrier: Type[PathCarrier] = PathCarrier
    blueprint: Type[PathBlueprint] = PathBlueprint