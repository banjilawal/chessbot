# src/domain/metadata/nulls/model/alert/group.py

"""
Module: domain.metadata.nulls.model.alert.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Alert, ModelNullWarningSet
from err import (
    AlertBlueprintNullException, AlertCarrierNullException, AlertNullException
)


class AlertNullWarningSet(ModelNullWarningSet[Alert]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Alert's integrity cycle.

    Attributes:
        model: AlertNullException
        carrier: AlertCarrierNullException
        blueprint: AlertBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[AlertNullException] | None = None,
            carrier: Optional[AlertCarrierNullException] | None = None,
            blueprint: Optional[AlertBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[AlertNullException]
            carrier: Optional[AlertCarrierNullException]
            blueprint: Optional[AlertBlueprintNullException]
        """
        super().__init__(
            model = model or AlertNullException(),
            carrier = carrier or AlertCarrierNullException(),
            blueprint = blueprint or AlertBlueprintNullException(),
        )
        
    @property
    def model(self) -> AlertNullException:
        return cast(AlertNullException, super().model)
    
    @property
    def carrier(self) -> AlertCarrierNullException:
        return cast(AlertCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AlertBlueprintNullException:
        return cast(AlertBlueprintNullException, super().blueprint)