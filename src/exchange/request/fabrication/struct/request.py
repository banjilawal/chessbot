# src/exchange/request/fabrication/struct/request.py

"""
Module: exchange.request.fabrication.struct.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Generic, TypeVar, cast

from domain import Struct
from exchange import BuildRequest
from transit import StructCarrier

T = TypeVar("T", bound="Struct")

class StructBuildRequest(BuildRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a BuildOperation needs to run a job.

     Attributes:
         id: int
         item: StructCarrier[T]

     Provides:
     
     Super Class:
        BuildRequest
     """
    
    def __init__(self, id: int, item: StructCarrier[T]):
        """
        Args:
            id: int
            item: StructCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> StructCarrier[T]:
        return cast(StructCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StructBuildRequest):
            return self.id == other.id
        return False