# src/assurance/depend/toolkit/model/account/toolkit.py

"""
Module: assurance.depend.toolkit.model.account.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import AccountServiceDependency, ModelLayerToolkit
from domain import Account, AccountLayer, AccountManifest, AccountNullWarningSet


class AccountLayerToolkit(ModelLayerToolkit[Account]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Account attribute validators and type manifest.

    Attributes:
        helper: AccountManifest
        manifest: AccountServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[AccountManifest] | None = None,
            dependency: Optional[AccountServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[AccountManifest]
            manifest: Optional[AccountServiceDependency]
        """
        super().__init__(
            dependency=dependency or AccountServiceDependency(),
            manifest=manifest or AccountManifest(),
        )
    
    @property
    def dependency(self) -> AccountServiceDependency:
        return cast(AccountServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> AccountManifest:
        return cast(AccountManifest, super().manifest)
    
    @property
    def nulls(self) -> AccountNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> AccountLayer:
        return self.manifest.types