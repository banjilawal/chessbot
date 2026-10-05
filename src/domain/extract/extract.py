# src/domain/extract.py

"""
Module: domain.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from domain import Blueprint
from transit import EntityCarrier

T = TypeVar("T")

class PrimeExtract(ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for Validator.

    Attributes:
        carrier: EntityCarrier[T]
        blueprint: Optional[Blueprint[T]]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
    """
    _carrier: EntityCarrier[T]
    _blueprint: Optional[Blueprint[T]]

    def __init__(
            self,
            carrier: EntityCarrier[T],
            blueprint: Optional[Blueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[T]
            blueprint: Optional[Blueprint[T]]
        """
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def carrier(self) -> EntityCarrier[T]:
        return self._carrier
    
    @property
    def blueprint(self) -> Optional[Blueprint[T]]:
        return self._blueprint
    
    @property
    def recipient_wants_model(self) -> bool:
        return self.no_blueprint_exists and self._carrier.has_model
    
    @property
    def recipient_wants_blueprint(self) -> bool:
        return self.blueprint_exists and self._carrier.has_blueprint
    
    @property
    def blueprint_exists(self) -> bool:
        return self._blueprint is None
    
    @property
    def no_blueprint_exists(self) -> bool:
        return not self.blueprint_exists