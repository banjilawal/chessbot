# src/domain/metadata/manifest/model/alert/manifest.py

"""
Module: domain.metadata.manifest.model.alert.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AlertTable, AlertTableNullGroup, AlertTableTypeUnion, ModelManifest


class AlertTableManifest(ModelManifest[AlertTable]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the AlertTable security lifecycle.

     Attributes:
        types: AlertTableTypeUnion
        nulls: AlertTableNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[AlertTableTypeUnion] | None = None,
            nulls: Optional[AlertTableNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[AlertTableTypeUnion]
            nulls: Optional[AlertTableNullGroup]
        """
        super().__init__(
            types=types or AlertTableTypeUnion(),
            nulls=nulls or AlertTableNullGroup(),
        )
        
    @property
    def types(self) -> AlertTableTypeUnion:
        return cast(AlertTableTypeUnion, super().types)
    
    @property
    def nulls(self) -> AlertTableNullGroup:
        return cast(AlertTableNullGroup, super().nulls)