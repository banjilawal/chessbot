# src/domain/exchange/request/validation/model/request.py

"""
Module: domain.exchange.request.validation.model.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Model, ValidationRequest
from transit import EntityCarrier

T = TypeVar("T", bound="Model")


class ModelValidationRequest(ValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         - Messaging
         - Transport

     Responsibilities:
        1. Transport the collection and other objects a ValidationOperation needs to run a job.

     Attributes:
         id: int
         carriery: EntityCarrier[T]

     Provides:
     
     Super Class:
        Request
     """
    _item: EntityCarrier[T]
    
    def __init__(self, id: int, item: EntityCarrier[T]):
        """
        Args:
            id: int
            item: EntityCarrier[T]
        """
        super().__init__(id=id)
        self._item = item
    
    @property
    def item(self) -> EntityCarrier[T]:
        return self._item
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ModelValidationRequest):
            return self.id == other.id
        return False