# src/domain/metadata/context/manifest/context/account/account/manifest.py

"""
Module: domain.metadata.manifest.context.account.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AccountContext, AccountContextNullGroup, AccountContextTypeUnion


class AccountContextManifest(ContextManifest[AccountContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Account
            security lifecycle.

     Attributes:
        types: AccountContextTypeUnion
        nulls: AccountContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """

    def __init__(
            self,
            types: Optional[AccountContextTypeUnion] | None = None,
            nulls: Optional[AccountContextNullGroup] | None = None,
    ):
        """
        Args:
            types: AccountContextTypeUnion
            nulls: AccountContextNullGroup
        """
        super().__init__(
            types=types or AccountContextTypeUnion(),
            nulls=nulls or AccountContextNullGroup(),
        )

    @property
    def types(self) -> AccountContextTypeUnion:
        return cast(AccountContextTypeUnion, super().types)

    @property
    def nulls(self) -> AccountContextNullGroup:
        return cast(AccountContextNullGroup, super().nulls)