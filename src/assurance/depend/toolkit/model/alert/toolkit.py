# src/assurance/depend/toolkit/model/alert/toolkit.py

"""
Module: assurance.depend.toolkit.model.alert.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, AlertServiceDependency
from domain import Alert, AlertManifest, AlertNullWarningSet, AlertLayer

class AlertLayerToolkit(ModelLayerToolkit[Alert]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Alert attribute validators and type manifest.

    Attributes:
        helper: AlertManifest
        manifest: AlertServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[AlertManifest] | None = None,
            dependency: Optional[AlertServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[AlertManifest]
            manifest: Optional[AlertServiceDependency]
        """
        super().__init__(
            dependency=dependency or AlertServiceDependency(),
            manifest=manifest or AlertManifest(),
        )
    
    @property
    def dependency(self) -> AlertServiceDependency:
        return cast(AlertServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> AlertManifest:
        return cast(AlertManifest, super().manifest)
    
    @property
    def nulls(self) -> AlertNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> AlertLayer:
        return self.manifest.types