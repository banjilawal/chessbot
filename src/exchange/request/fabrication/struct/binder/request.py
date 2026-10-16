# src/exchange/request/fabrication/struct/binder/request.py

"""
Module: exchange.request.fabrication.struct.binder.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import ArchetypeBinder
from exchange import StructBuildRequest
from transit import BinderCarrier

T = TypeVar("T", bound="ArchetypeBinder")


class BinderBuildRequest(StructBuildRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a BinderValidator needs to run a job.

     Attributes:
         id: int
         item: BinderCarrier[T]

     Provides:
     
     Super Class:
        BuildRequest
     """
    
    def __init__(self, id: int, item: BinderCarrier[T]):
        """
        Args:
            id: int
            item: BinderCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> BinderCarrier[T]:
        return cast(BinderCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BinderBuildRequest):
            return self.id == other.id
        return False