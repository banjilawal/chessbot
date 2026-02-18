# src/chess/graph/edge/service/service.py

"""
Module: chess.graph.edge.service.service
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.system import EntityService, IdFactory
from chess.graph import Edge, EdgeBuilder, EdgeValidator


class EdgeService(EntityService[Edge]):
    """
    """
    SERVICE_NAME = "EdgeService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: EdgeBuilder = EdgeBuilder(),
            validator: EdgeValidator = EdgeValidator(),
            id: int = IdFactory.next_id(class_name="EdgeService"),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> EdgeBuilder:
        return cast(EdgeBuilder, self.entity_builder)
    
    @property
    def validator(self) -> EdgeValidator:
        return cast(EdgeValidator, self.entity_validator)