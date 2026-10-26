# src/domain/metadata/manifest/model/account/machine/manifest.py

"""
Module: domain.metadata.manifest.model.account.machine.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    MachineAccountNullWarningSet, MachineAccount, MachineAccountLayer, AccountManifest
)


class MachineAccountManifest(AccountManifest[MachineAccount]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the MachineAccount 
            security lifecycle.

     Attributes:
        types: MachineAccountTypeUnion
        nulls: MachineAccountNullGroup

     Provides:

     Super Class:
        AccountManifest
     """
    
    def __init__(
            self,
            types: Optional[MachineAccountLayer] | None = None,
            nulls: Optional[MachineAccountNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[MachineAccountTypeUnion]
            nulls: Optional[MachineAccountNullGroup]
        """
        super().__init__(
            types=types or MachineAccountLayer(),
            nulls=nulls or MachineAccountNullWarningSet(),
        )
    
    @property
    def types(self) -> MachineAccountLayer:
        return cast(MachineAccountLayer, super().types)
    
    @property
    def nulls(self) -> MachineAccountNullWarningSet:
        return cast(MachineAccountNullWarningSet, super().nulls)