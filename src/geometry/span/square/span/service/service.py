# src/geometry/span/square/span/service/validator.py

"""
Module: geometry.span.square.span.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from math.span import SquareSpan, SquareSpanBuilder, SquareSpanValidator
from system import IdFactory, IntegrityMicroservice


class SquareSpanService(IntegrityMicroservice[SquareSpan]):
    """
    ROLE: Microservice, Computation
    TASK: Graphing
    
    RESPONSIBILITIES:
        1.  Generate a Graph from a Token's current position.
    
    INHERITED RESPONSIBILITIES:
        * See Microservice for inherited responsibilities.
    
    PARENT:
        *   Microservice
    
    PROVIDES:
    None
    
    LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See IntegrityMicroservice for inherited attributes.
    
    CONSTRUCTOR PARAMETERS:
        *   id: int
        *   schema: str
        *   coord_service: CoordService
        *   vector_service: VectorService
    
    LOCAL METHODS:
    None
    
    INHERITED METHODS:
        *   See IntegrityMicroservice for inherited methods.
    """
    SERVICE_NAME = "SquareSpanService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareSpanBuilder = SquareSpanBuilder(),
            validator: SquareSpanValidator = SquareSpanValidator(),
            id: int = IdFactory.next_id(class_name="SquareSpanService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: SquareSpanBuilder
            validator: SquareSpanValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> SquareSpanBuilder:
        return cast(SquareSpanBuilder, self.builder)
    
    @property
    def validator(self) -> SquareSpanValidator:
        return cast(SquareSpanValidator, self.validator)