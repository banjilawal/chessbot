# src/logic/span/square/ray/service/validator.py

"""
Module: logic.span.square.ray.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.span import SquareRay, SquareRayBuilder, SquareRayValidator
from logic.system import IdFactory, IntegrityMicroService


class SquareRayService(IntegrityMicroService[SquareRay]):
    """
    ROLE: MicroService, Computation
    TASK: Graphing
    
    RESPONSIBILITIES:
        1.  Generate a Graph from a Token's current position.
    
    INHERITED RESPONSIBILITIES:
        * See MicroService for inherited responsibilities.
    
    PARENT:
        *   MicroService
    
    PROVIDES:
    None
    
    LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See IntegrityMicroService for inherited attributes.
    
    CONSTRUCTOR PARAMETERS:
        *   id: int
        *   name: str
        *   coord_service: CoordService
        *   vector_service: VectorService
    
    LOCAL METHODS:
    None
    
    INHERITED METHODS:
        *   See IntegrityMicroService for inherited methods.
    """
    SERVICE_NAME = "SquareRayService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareRayBuilder = SquareRayBuilder(),
            validator: SquareRayValidator = SquareRayValidator(),
            id: int = IdFactory.next_id(class_name="SquareRayService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: SquareRayBuilder
            validator: SquareRayValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> SquareRayBuilder:
        return cast(SquareRayBuilder, self.builder)
    
    @property
    def validator(self) -> SquareRayValidator:
        return cast(SquareRayValidator, self.validator)