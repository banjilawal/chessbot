# src/assurance/depend/toolkit/model/alert/toolkit.py

"""
Module: assurance.depend.toolkit.model.alert.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, AlertTableWrapperDependency
from domain import AlertTable, AlertTableManifest, AlertTableNullGroup, AlertTableTypeUnion

class AlertTableValidatorToolkit(ModelValidatorToolkit[AlertTable]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for AlertTable attribute validators and type metadata.

    Attributes:
        helper: AlertTableManifest
        metadata: AlertTableWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[AlertTableManifest] | None = None,
            wrapper: Optional[AlertTableWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[AlertTableManifest]
            metadata: Optional[AlertTableWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or AlertTableWrapperDependency(),
            metadata=metadata or AlertTableManifest(),
        )
    
    @property
    def wrapper(self) -> AlertTableWrapperDependency:
        return cast(AlertTableWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> AlertTableManifest:
        return cast(AlertTableManifest, super().metadata)
    
    @property
    def nulls(self) -> AlertTableNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> AlertTableTypeUnion:
        return self.metadata.types