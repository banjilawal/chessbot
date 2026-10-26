# src/domain/metadata/nulls/context/group.py

"""
Module: domain.metadata.nulls.context.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Context, NullExceptionGroup
from err import ContextCarrierNullException, ContextBlueprintNullException, ContextNullException

T = TypeVar("T", bound="Context")

class ContextNullGroup(NullExceptionGroup[T], ABC, Generic[T):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Context's integrity cycle.

    Attributes:
        model: ContextNullException
        carrier: ContextCarrierNullException
        blueprint: ContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: ContextNullException,
            carrier: ContextCarrierNullException,
            blueprint: ContextBlueprintNullException,
    ):
        """
        Args:
            model: ContextNullException
            carrier: ContextCarrierNullException
            blueprint: ContextBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)

        
    @property
    def model(self) -> ContextNullException:
        return cast(ContextNullException, super().model)
    
    @property
    def carrier(self) -> ContextCarrierNullException:
        return cast(ContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ContextBlueprintNullException:
        return cast(ContextBlueprintNullException, super().blueprint)