# src/domain/metadata/null/context/null.py

"""
Module: domain.metadata.null.context.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Context, NullWarningSet
from err import BlueprintNullException, ContextNullException, EntityCarrierNullException

T = TypeVar("T", bound="Context")

class ContextNullWarningSet(NullWarningSet[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Context's integrity cycle.

    Attributes:
        model: ContextNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: ContextNullException,
            carrier: EntityCarrierNullException,
            blueprint: BlueprintNullException,
    ):
        """
        Args:
            model: ContextNullException
            carrier: EntityCarrierNullException
            blueprint: BlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)

        
    @property
    def model(self) -> ContextNullException:
        return cast(ContextNullException, super().model)
    
    @property
    def carrier(self) -> EntityCarrierNullException:
        return cast(EntityCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BlueprintNullException:
        return cast(BlueprintNullException, super().blueprint)