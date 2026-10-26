# src/assurance/depend/toolkit/model/alert/toolkit.py

"""
Module: assurance.depend.toolkit.model.alert.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, AlertWrapperDependency
from domain import Alert, AlertManifest, AlertNullWarningSet, AlertLayer

class AlertValidatorToolkit(ModelValidatorToolkit[Alert]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Alert attribute validators and type metadata.

    Attributes:
        helper: AlertManifest
        metadata: AlertWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[AlertManifest] | None = None,
            wrapper: Optional[AlertWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[AlertManifest]
            metadata: Optional[AlertWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or AlertWrapperDependency(),
            metadata=metadata or AlertManifest(),
        )
    
    @property
    def wrapper(self) -> AlertWrapperDependency:
        return cast(AlertWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> AlertManifest:
        return cast(AlertManifest, super().metadata)
    
    @property
    def nulls(self) -> AlertNullWarningSet:
        return self.metadata.nulls
    
    @property
    def types(self) -> AlertLayer:
        return self.metadata.types