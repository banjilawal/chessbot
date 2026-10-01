# src/domain/metadata/manifest/model/account/account/manifest.py

"""
Module: domain.metadata.manifest.model.account.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelManifest, Account, AccountNullGroup, AccountTypeUnion

T = TypeVar("T", bound="Account")

class AccountManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Account
            security lifecycle.

     Attributes:
        types: AccountTypeUnion[T]
        nulls: AccountNullGroup[T]

     Provides:

     Super Class:
        ModelManifest
     """

    def __init__(
            self,
            types: Optional[AccountTypeUnion[T]] | None = None,
            nulls: Optional[AccountNullGroup[T]] | None = None,
    ):
        """
        Args:
            types: AccountTypeUnion[T]
            nulls: AccountNullGroup[T]
        """
        super().__init__(
            types=types or AccountTypeUnion(),
            nulls=nulls or AccountNullGroup(),
        )

    @property
    def types(self) -> AccountTypeUnion[T]:
        return cast(AccountTypeUnion[T], super().types)

    @property
    def nulls(self) -> AccountNullGroup[T]:
        return cast(AccountNullGroup[T], super().nulls)