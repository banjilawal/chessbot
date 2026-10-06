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
        reference: EntityCarrier[T]
        blueprint: Optional[Blueprint[T]]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool
        recipient_wants_model: bool
        recipient_wants_blueprint: bool

    Super Class:
    """
    _reference: EntityCarrier[T]
    _blueprint: Optional[Blueprint[T]]

    def __init__(
            self,
            reference: EntityCarrier[T],
            blueprint: Optional[Blueprint[T]],
    ):
        """
        Args:
            reference: EntityCarrier[T]
            blueprint: Optional[Blueprint[T]]
        """
        self._reference = reference
        self._blueprint = blueprint
        
    @property
    def reference(self) -> EntityCarrier[T]:
        return self._reference
    
    @property
    def blueprint(self) -> Optional[Blueprint[T]]:
        return self._blueprint
    
    @property
    def recipient_wants_model(self) -> bool:
        return (
                self._reference.has_model and
                self.blueprint_does_not_exist
        )
    
    @property
    def recipient_wants_blueprint(self) -> bool:
        return (
                self._reference.has_blueprint and
                self.blueprint_exists
        )
    
    @property
    def blueprint_exists(self) -> bool:
        return self._blueprint is not None
    
    @property
    def blueprint_does_not_exist(self):
        return not self.blueprint_exists
