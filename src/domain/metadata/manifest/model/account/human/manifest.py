# src/domain/metadata/manifest/model/account/human/manifest.py

"""
Module: domain.metadata.manifest.model.account.human.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    HumanAccountNullGroup, HumanAccount, HumanAccountLayer, AccountManifest
)


class HumanAccountManifest(AccountManifest[HumanAccount]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the HumanAccount 
            security lifecycle.

     Attributes:
        types: HumanAccountTypeUnion
        nulls: HumanAccountNullGroup

     Provides:

     Super Class:
        AccountManifest
     """
    
    def __init__(
            self,
            types: Optional[HumanAccountLayer] | None = None,
            nulls: Optional[HumanAccountNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[HumanAccountTypeUnion]
            nulls: Optional[HumanAccountNullGroup]
        """
        super().__init__(
            types=types or HumanAccountLayer(),
            nulls=nulls or HumanAccountNullGroup(),
        )
    
    @property
    def types(self) -> HumanAccountLayer:
        return cast(HumanAccountLayer, super().types)
    
    @property
    def nulls(self) -> HumanAccountNullGroup:
        return cast(HumanAccountNullGroup, super().nulls)