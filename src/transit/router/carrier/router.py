# src/transit/route/carrier/router.py

"""
Module: transit.route.carrier.route
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import Blueprint, Model, ModelBlueprint
from transit import Router

T = TypeVar("T", bound="Model")

class CarrierRouter(Router[T], ABC, Generic[T]):
    """
    Role
        -   Routing

    Responsibilities:
        1.  Ensure data-holders are safe before they are used or saved.

    Attributes:
        model: Optional[T]
        blueprint: Optional[ModelBlueprint[T]]
        
    Provides:
        - route(*args, **kwargs) -> Any

    super Class:
        Router
    """
    _model: Optional[T]
    _blueprint: Optional[ModelBlueprint[T]]
    
    def __init__(
            self,
            model: Optional[T],
            blueprint: Optional[ModelBlueprint[T]],
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[ModelBlueprint[T]]
        """
        
    @property
    def model(self) -> Optional[T]:
        return self._model
    
    @property
    def blueprint(self) -> Optional[ModelBlueprint[T]]:
        return self._blueprint
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | ModelBlueprint[T]]:
        pass
    
    @abstractmethod
    def has_blueprint(self) -> bool:
        pass
    
    @abstractmethod
    def has_model(self) -> bool:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass
    