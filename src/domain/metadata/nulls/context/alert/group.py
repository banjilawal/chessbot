# src/domain/metadata/nulls/context/alert/group.py

"""
Module: domain.metadata.nulls.context.alert.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Alert, ContextNullGroup
from err import (
    AlertContextBlueprintNullException, AlertContextCarrierNullException, AlertContextNullException
)


class AlertContextNullGroup(ContextNullGroup[AlertContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Alert's integrity cycle.

    Attributes:
        context: AlertContextNullException
        carrier: AlertContextCarrierNullException
        blueprint: AlertContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[AlertContextNullException] | None = None,
            carrier: Optional[AlertContextCarrierNullException] | None = None,
            blueprint: Optional[AlertContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[AlertContextNullException]
            carrier: Optional[AlertContextCarrierNullException]
            blueprint: Optional[AlertContextBlueprintNullException]
        """
        super().__init__(
            context = context or AlertContextNullException(),
            carrier = carrier or AlertContextCarrierNullException(),
            blueprint = blueprint or AlertContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> AlertContextNullException:
        return cast(AlertContextNullException, super().context)
    
    @property
    def carrier(self) -> AlertContextCarrierNullException:
        return cast(AlertContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AlertContextBlueprintNullException:
        return cast(AlertContextBlueprintNullException, super().blueprint)