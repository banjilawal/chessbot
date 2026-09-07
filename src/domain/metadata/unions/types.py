# src/domain/metadata/unions/manifest.py

"""
Module: domain.metadata.unions.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar

from domain import Blueprint, DomainDataObject
from transit import EntityCarrier

T = TypeVar("T", bound="DomainDataObject")


class TypeUnion(ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a DomainObject.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]
        
    Provides:

    Super Class:
    """
    _model: Type[T]
    _carrier: Type[EntityCarrier[T]]
    _blueprint: Type[Blueprint[T]]
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[EntityCarrier[T]],
            blueprint: Type[Blueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[Blueprint[T]]
        """
        self._model = model
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def model(self) -> Type[T]:
        return self._model
    
    @property
    def carrier(self) -> Type[EntityCarrier[T]]:
        return self._carrier
    
    @property
    def blueprint(self) -> Type[Blueprint[T]]:
        return self._blueprint