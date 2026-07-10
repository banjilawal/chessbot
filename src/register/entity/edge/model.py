# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import EdgeNullException
from model import EntityRegister, Edge


class EdgeEntityRegister(EntityRegister[Edge]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Edge
        null_exception: EdgeNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Edge = Type[Edge],
            null_exception: EdgeNullException = EdgeNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Edge:
        return cast(Edge, self.a)
    
    @property
    def null_exception(self) -> EdgeNullException:
        return cast(EdgeNullException, self.null_exception)
    
    @property
    def edge(self) -> Edge:
        return self.model
    
    @property
    def is_edge_entity_register(self) -> bool:
        return isinstance(self, EdgeEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EdgeEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
