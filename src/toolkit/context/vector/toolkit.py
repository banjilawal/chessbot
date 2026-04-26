# src/toolkit/context/vector/toolkit.py

"""
Module: toolkit.context.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator
from microservice import CoordService, ScalarService, VectorService
from model import VectorOperand
from toolkit import Toolkit


class VectorOperandToolkit(Toolkit[VectorOperand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Set of workers and services common to VectorContext
            Builder and Validator.

    Attributes:
        coord_service: CoordService
        vector_service: VectorService
        scalar_service: ScalarService
        number_validator: NumberValidator

    Provides:

    Super Class:
    Toolkit
    """
    _coord_service: CoordService
    _vector_service: VectorService
    _scalar_service: ScalarService
    _number_validator: NumberValidator
   
    def __init__(
            self,
            coord_service: CoordService = None,
            vector_service: VectorService = None,
            scalar_service: ScalarService = None,
            number_validator: NumberValidator = None,
    ):
        """
        Args:
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        """
        if coord_service is None:
            coord_service = CoordService()
        if vector_service is None:
            vector_service = VectorService()
        if scalar_service is None:
            scalar_service = ScalarService()
        if number_validator is None:
            number_validator = NumberValidator()
            
        self._coord_service = coord_service
        self._vector_service = vector_service
        self._scalar_service = scalar_service
        self._number_validator = number_validator
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def scalar_service(self) -> ScalarService:
        return self._scalar_service

    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    

        
