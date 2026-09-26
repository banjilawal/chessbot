# src/exchange/request/validation/model/request.py

"""
Module: exchange.request.validation.model.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from exchange import ValidationRequest
from domain import Model
from transit import ModelCarrier

T = TypeVar("T", bound="Model")


class ModelValidationRequest(ValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a Model validation job.

     Attributes:
         id: int
         item: ModelCarrier[T]

     Provides:
     
     Super Class:
        ValidationRequest
     """
    _item: ModelCarrier[T]
    
    def __init__(self, id: int, item: ModelCarrier[T]):
        """
        Args:
            id: int
            item: ModelCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> ModelCarrier[T]:
        return cast(ModelCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ModelValidationRequest):
            return self.id == other.id
        return False