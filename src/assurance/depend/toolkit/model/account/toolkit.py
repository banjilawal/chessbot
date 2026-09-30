# src/assurance/depend/toolkit/model/account/toolkit.py

"""
Module: assurance.depend.toolkit.model.account.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, AccountWrapperDependency
from domain import Account, AccountManifest, AccountNullGroup, AccountTypeUnion


class AccountValidatorToolkit(ModelValidatorToolkit[Account]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Account attribute validators and type metadata.

    Attributes:
        helper: AccountManifest
        metadata: AccountHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[AccountManifest] | None = None,
            wrapper: Optional[AccountWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[AccountManifest]
            metadata: Optional[AccountHelperTable]
        """
        super().__init__(
            wrapper=wrapper or AccountWrapperDependency(),
            metadata=metadata or AccountManifest(),
        )
    
    @property
    def wrapper(self) -> AccountWrapperDependency:
        return cast(AccountWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> AccountManifest:
        return cast(AccountManifest, super().metadata)
    
    @property
    def nulls(self) -> AccountNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> AccountTypeUnion:
        return self.metadata.types