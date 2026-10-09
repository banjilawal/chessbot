# src/domain/extract/model/alert/extract.py

"""
Module: domain.extract.model.alert.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Alert, AlertBlueprint, ModelPrimeExtract
from transit import AlertCarrier


class AlertPrimeExtract(ModelPrimeExtract[Alert]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for AlertValidator.

    Attributes:
        carrier: AlertCarrier
        blueprint: Optional[AlertBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: AlertCarrier,
            blueprint: Optional[AlertBlueprint] | None = None,
    ):
        """
        Args:
            reference: AlertCarrier
            blueprint: Optional[Blueprint[Alert]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> AlertCarrier:
        return cast(AlertCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[AlertBlueprint]:
        return cast(AlertBlueprint, super().blueprint)