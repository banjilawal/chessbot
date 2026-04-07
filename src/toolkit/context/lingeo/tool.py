# src/tool/algebra/tool.py

"""
Module: tool.algebra.tool
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import NumberValidator
from microservice import CoordService, ScalarService, VectorService
from model import LinGeoContext
from tool import toolkit


class LinGeoContexttoolkit(toolkit[LinGeoContext]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Set of workers and services common to LinGeoContext
            Builder and Validator.

    Attributes:
        coord_service: CoordService
        vector_service: VectorService
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
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            scalar_service: ScalarService = ScalarService(),
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
    

        
