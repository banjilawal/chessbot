# src/domain/metadata/context/manifest/context/account/account/manifest.py

"""
Module: domain.metadata.manifest.context.account.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AccountContext, AccountContextNullWarningSet, AccountContextLayer


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
            types: Optional[AccountContextLayer] | None = None,
            nulls: Optional[AccountContextNullWarningSet] | None = None,
    ):
        """
        Args:
            types: AccountContextTypeUnion
            nulls: AccountContextNullGroup
        """
        super().__init__(
            types=types or AccountContextLayer(),
            nulls=nulls or AccountContextNullWarningSet(),
        )

    @property
    def types(self) -> AccountContextLayer:
        return cast(AccountContextLayer, super().types)

    @property
    def nulls(self) -> AccountContextNullWarningSet:
        return cast(AccountContextNullWarningSet, super().nulls)