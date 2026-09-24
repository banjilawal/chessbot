# src/domain/metadata/nulls/roster.py

"""
Module: domain.metadata.nulls.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from err import BlueprintNullException, EntityCarrierNullException, NullException

T = TypeVar("T")

@dataclass
class NullExceptionGroup(ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a DomainObject

    Attributes:
        model: NullException
        blueprint: BlueprintNullException
        carrier: EntityCarrierNullException

    Provides:

    Super Class:
    """
    _model: NullException
    _blueprint: BlueprintNullException
    _carrier: EntityCarrierNullException

    
    def __init__(
            self,
            model: NullException,
            blueprint: BlueprintNullException,
            carrier: EntityCarrierNullException,
    ):
        """
        Args:
            model: NullException
            blueprint: BlueprintNullException
            carrier: EntityCarrierNullException
        """
        self._model = model
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def model(self) -> NullException:
        return self._model
    
    @property
    def blueprint(self) -> BlueprintNullException:
        return self._blueprint
    
    @property
    def carrier(self) -> EntityCarrierNullException:
        return self._carrier
        