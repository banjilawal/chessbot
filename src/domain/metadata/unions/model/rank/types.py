# src/domain/metadata/unions/model/rank/types.py

"""
Module: domain.metadata.unions.rank.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ModelTypeUnion, Rank, RankBlueprint
from transit import RankCarrier

T = TypeVar("T", bound="Rank")


class RankTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Rank.

    Attributes:
        model: Type[T]
        carrier: Type[RankCarrier[T]]
        blueprint: Type[RankBlueprint[T]]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[T]] | None = None,
            carrier: Optional[Type[RankCarrier[T]]] | None = None,
            blueprint: Optional[Type[RankBlueprint[T]]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[T]]
            carrier: Optional[Type[RankCarrier[T]]]
            blueprint: Optional[Type[RankBlueprint[T]]]
        """
        super().__init__(
            model=model or Type[Rank],
            carrier=carrier or Type[RankCarrier],
            blueprint=blueprint or Type[RankBlueprint],
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[RankCarrier[T]]:
        return cast(Type[RankCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[RankBlueprint[T]]:
        return cast(Type[RankBlueprint[T]], super().blueprint)