# src/assurance/manifest/types/rank/manifest.py

"""
Module: assurance.manifest.types.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import RankBlueprint
from model import Rank
from transit import RankCarrier


@dataclass(frozen=True)
class RankTypes(TypesManifest[Rank]):
    model: Type[Rank] = Rank
    carrier: Type[RankCarrier] = RankCarrier
    blueprint: Type[RankBlueprint] = RankBlueprint