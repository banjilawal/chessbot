# src/logic/span/square/ray/service/transaction.py

"""
Module: logic.span.square.ray.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.span import SquareRay, SquareRayBuildTransaction, SquareRayValidationTransaction
from logic.system import IdFactory, IntegrityService


class SquareRayService(IntegrityService[SquareRay]):
    """
    ROLE: Service, Computation
    TASK: Graphing
    
    RESPONSIBILITIES:
        1.  Generate a Graph from a Token's current position.
    
    INHERITED RESPONSIBILITIES:
        * See Service for inherited responsibilities.
    
    PARENT:
        *   Service
    
    PROVIDES:
    None
    
    LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    
    CONSTRUCTOR PARAMETERS:
        *   id: int
        *   name: str
        *   coord_service: CoordService
        *   vector_service: VectorService
    
    LOCAL METHODS:
    None
    
    INHERITED METHODS:
        *   See IntegrityService for inherited methods.
    """
    SERVICE_NAME = "SquareRayService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareRayBuildTransaction = SquareRayBuildTransaction(),
            validator: SquareRayValidationTransaction = SquareRayValidationTransaction(),
            id: int = IdFactory.next_id(class_name="SquareRayService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: SquareRayBuildTransaction
            validator: SquareRayValidationTransaction
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def build(self) -> SquareRayBuildTransaction:
        return cast(SquareRayBuildTransaction, self.build)
    
    @property
    def validation(self) -> SquareRayValidationTransaction:
        return cast(SquareRayValidationTransaction, self.validation)