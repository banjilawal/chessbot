# src/chess/coord/service.py

"""
Module: chess.coord
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import Any

from chess.coord import Coord, CoordBuilder, CoordValidator
from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, ValidationResult
from chess.vector import Vector, VectorService


class CoordService:
    
    _coord_builder: type[CoordBuilder]
    _coord_validator: type[CoordValidator]
    _scalar_service: type[ScalarService]
    _vector_service: type[VectorService]
    
    def __init__(
            self,
            coord_builder: type[CoordBuilder],
            coord_validator: type[CoordValidator],
            scalar_service: type[ScalarService],
            vector_service: type[VectorService]
    ):
        self._coord_builder = coord_builder
        self._coord_validator = coord_validator
        self._scalar_service = scalar_service
        self._vector_service = vector_service
        
    
    def validate_as_coord(self, candidate: Any) -> ValidationResult[Coord]:
        return self._coord_validator.validate(candidate=candidate)
    
    
    def build_coord(self, row: int, column: int) -> BuildResult[Coord]:
        return self._coord_builder.build(row=row, column=column)
    
    
    def add_vector(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column + vector.x
            row = coord.row + vector.y
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
    
    def dot_product(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            column = coord.column * vector.y
            row = coord.row * vector.x
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
        
        
    def scalar_product(self, coord: Coord, scalar: Scalar) -> BuildResult[Coord]:
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            scalar_validation = self._scalar_service.validate_as_scalar(candidate=scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            row = coord.y * scalar.value
            column = coord.x * scalar.value
            
            return self._coord_builder.build(row=row, column=column)
        except Exception as ex:
            return BuildResult.failure(ex)
        
        
    def convert_vector_to_coord(self, vector: Vector) -> BuildResult[Coord]:
        try:
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            return self._coord_builder.build(row=vector.y, column=vector.x)
        except Exception as ex:
            return BuildResult.failure(ex)
        
    def convert_coord_to_vector(self, coord: Coord) -> BuildResult[Vector]:
        try:
            coord_validation = self._coord_validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            return self._vector_service.build_vector(y=coord.row, x=coord.column)
        except Exception as ex:
            return BuildResult.failure(ex)