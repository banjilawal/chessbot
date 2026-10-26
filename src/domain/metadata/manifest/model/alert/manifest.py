# src/domain/metadata/manifest/model/alert/manifest.py

"""
Module: domain.metadata.manifest.model.alert.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Alert, AlertNullGroup, AlertLayer, ModelManifest


class AlertManifest(ModelManifest[Alert]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Alert security lifecycle.

     Attributes:
        types: AlertTypeUnion
        nulls: AlertNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[AlertLayer] | None = None,
            nulls: Optional[AlertNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[AlertTypeUnion]
            nulls: Optional[AlertNullGroup]
        """
        super().__init__(
            types=types or AlertLayer(),
            nulls=nulls or AlertNullGroup(),
        )
        
    @property
    def types(self) -> AlertLayer:
        return cast(AlertLayer, super().types)
    
    @property
    def nulls(self) -> AlertNullGroup:
        return cast(AlertNullGroup, super().nulls)