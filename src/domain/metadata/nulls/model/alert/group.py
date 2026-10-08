# src/domain/metadata/nulls/model/alert/group.py

"""
Module: domain.metadata.nulls.model.alert.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AlertTable, ModelNullGroup
from err import (
    AlertTableBlueprintNullException, AlertTableCarrierNullException, AlertTableNullException
)


class AlertTableNullGroup(ModelNullGroup[AlertTable]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an AlertTable's integrity cycle.

    Attributes:
        model: AlertTableNullException
        carrier: AlertTableCarrierNullException
        blueprint: AlertTableBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[AlertTableNullException] | None = None,
            carrier: Optional[AlertTableCarrierNullException] | None = None,
            blueprint: Optional[AlertTableBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[AlertTableNullException]
            carrier: Optional[AlertTableCarrierNullException]
            blueprint: Optional[AlertTableBlueprintNullException]
        """
        super().__init__(
            model = model or AlertTableNullException(),
            carrier = carrier or AlertTableCarrierNullException(),
            blueprint = blueprint or AlertTableBlueprintNullException(),
        )
        
    @property
    def model(self) -> AlertTableNullException:
        return cast(AlertTableNullException, super().model)
    
    @property
    def carrier(self) -> AlertTableCarrierNullException:
        return cast(AlertTableCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AlertTableBlueprintNullException:
        return cast(AlertTableBlueprintNullException, super().blueprint)