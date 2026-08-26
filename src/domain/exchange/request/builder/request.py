# src/domain/exchange/request/builder/request.py

"""
Module: domain.exchange.request.builder.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast


from domain import DomainDataObject, Request
from transit import EntityCarrier

T = TypeVar("T", bound="DomainDataObject")



class BuildRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Transport the collection and other objects a BuilderOperation needs to run a job.

     Attributes:
         id: int
         carriert: EntityCarrier[T]

     Provides:
     
     Super Class:
        Request
     """
    _carrier: EntityCarrier[T]
    
    def __init__(self, id: int, carrier: EntityCarrier[T]):
        """
        Args:
            id: int
            carrier: EntityCarrier[T]
        """
        super().__init__(id=id)
        self._carrier = carrier
        
    @property
    def carrier(self) -> EntityCarrier[T]:
        return self._carrier
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BuildRequest):
            request = cast(BuildRequest, other)
            return self.id == request.id
        return False