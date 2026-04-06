# src/tool/algebra/tool.py

"""
Module: tool.algebra.tool
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from microservice import CoordService, VectorService
from model import AlgebraAcontext
from system import NumberValidator
from tool import ToolSet


class AlgebraTool(ToolSet[AlgebraAcontext]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the declarations of common security resources in Vector, Coord,
            and Scalar algebraic workers.

    Attributes:
        coord_service: CoordService
        vector_service: VectorService
        number_validator: NumberValidator

    Provides:

    Super Class:
    ToolSet
    """
    _coord_service: CoordService
    _vector_service: VectorService
    _number_validator: NumberValidator
   
    def __init__(
            self,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            number_validator: NumberValidator = NumberValidator(),
    ):
        """
        Args:
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        """
        self._coord_service = coord_service
        self._vector_service = vector_service
        self._number_validator = number_validator
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    

        
