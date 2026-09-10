# src/domain/metadata/manifest/cartesian/manifest.py

"""
Module: domain.metadata.manifest.cartesian.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Cartesian, CartesianNullGroup, CartesianTypeUnion, ObjectManifest


class CartesianManifest(ObjectManifest[Cartesian]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Cartesian's security lifecycle.

     Attributes:
        type_union: CartesianTypeUnion
        null_group: CartesianNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[CartesianTypeUnion] | None = None,
            null_group: Optional[CartesianNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[CartesianTypeUnion]
            null_group: Optional[CartesianNullGroup]
        """
        super().__init__(
            type_union=type_union or CartesianTypeUnion(),
            null_group=null_group or CartesianNullGroup(),
        )
        
    @property
    def types(self) -> CartesianTypeUnion:
        return cast(CartesianTypeUnion, super().types)
    
    @property
    def nulls(self) -> CartesianNullGroup:
        return cast(CartesianNullGroup, super().nulls)