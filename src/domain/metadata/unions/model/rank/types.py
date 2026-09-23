# src/domain/metadata/unions/rank/types.py

"""
Module: domain.metadata.unions.rank.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import Rank, RankBlueprint, TypeUnion
from transit import RankCarrier

T = TypeVar("T", bound="Rank")

class RankTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Rank.

    Attributes:
        model: Type[Rank]
        carrier: Type[RankCarrier]
        blueprint: Type[RankBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    pass