# src/logic/span/square/span/service/service.py

"""
Module: logic.span.square.span.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.span import SquareSpan, SquareSpanBuildProcess, SquareSpanValidationProcess
from logic.system import IdFactory, IntegrityService


class SquareSpanService(IntegrityService[SquareSpan]):
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
    SERVICE_NAME = "SquareSpanService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareSpanBuildProcess = SquareSpanBuildProcess(),
            validator: SquareSpanValidationProcess = SquareSpanValidationProcess(),
            id: int = IdFactory.next_id(class_name="SquareSpanService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: SquareSpanBuildProcess
            validator: SquareSpanValidationProcess
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> SquareSpanBuildProcess:
        return cast(SquareSpanBuildProcess, self.builder)
    
    @property
    def validator(self) -> SquareSpanValidationProcess:
        return cast(SquareSpanValidationProcess, self.validator)