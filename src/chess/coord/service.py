# src/chess/target/service.py

"""
Module: chess.target.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import Any, List

from chess.scalar import Scalar, ScalarService
from chess.vector import Vector, VectorService
from chess.system import BuildResult, LoggingLevelRouter, ValidationResult
from chess.coord import Coord, CoordBuilder, CoordValidator, CoordSearchService


class CoordService:
    """
    # ROLE: Service, Data Protraction

    # RESPONSIBILITIES:
    1.  Manages integrity lifecycle of Coord objects.
    2.  Vector addition and scalar multiplication of Coord objects.
    3.  Calculate distance between two Coords.

    # PROVIDES:
        *   CoordBuilder
        *   CoordValidator
        *   ScalarService
        *   VectorService

    # ATTRIBUTES:
        *   coord_builder (type[CoordBuilder]): produces safe Coord objects.
        *   coord_validator (type[CoordValidator]): ensures existing Coord objects are safe.
        
        *   scalar_service (type[ScalarService): Manages integrity of scalar objects.
        *   vector_service (type[VectorService]): Manages integrity of vector objects, scalar-vector multiplication.
    """
    
    _coord_builder: type[CoordBuilder]
    _coord_validator: type[CoordValidator]
    _scalar_service: ScalarService
    _vector_service: VectorService
    _search_service: type[CoordSearchService]
    
    def __init__(
            self,
            coord_builder: type[CoordBuilder] = CoordBuilder,
            coord_validator: type[CoordValidator] = CoordValidator,
            scalar_service: ScalarService = ScalarService(),
            vector_service: VectorService = VectorService(),
            search_service: type[CoordSearchService] = CoordSearchService
    ):
        self._coord_builder = coord_builder
        self._coord_validator = coord_validator
        self._scalar_service = scalar_service
        self._vector_service = vector_service
        self._search_service = search_service
        
    
    @property
    def validator(self) -> type[CoordValidator]:
        """Its ok to expose the validator directly. Its factory methods might be useful."""
        return self._coord_validator
        
    
    def validate_as_coord(self, candidate: Any) -> ValidationResult[Coord]:
        """
        # Action:
        CoordService directs coord_validator to run the verification process on the candidate.

        # Parameters:
            *   row (int):
            *   column (int):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   coord_validator sends any validation exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._coord_validator.validate(candidate=candidate)
    
    
    def build_coord(self, row: int, column: int) -> BuildResult[Coord]:
        """
        # Action:
        CoordService directs coord_builder to run the build process with the inputs.

        # Parameters:
            *   row (int):
            *   column (int):
            
        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   coord_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._coord_builder.build(row=row, column=column)
    
    
    def add_vector_to_coord(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  coord_validator runs integrity checks on the target param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and vector params are valid:
                new_row, new_colum = target.row + vector.y, target.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    coord_validator
                    vector_service
            *   coord_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.add_vector_to_coord"
        
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
        """
        # Action:
        1.  coord_validator runs integrity checks on the target param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and vector params are valid:
                new_row, new_colum = target.row + vector.y, target.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    coord_validator
                    vector_service
            *   coord_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.dot_product"
        
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
        
        
    def multiply_coord_by_scalar(self, coord: Coord, scalar: Scalar) -> BuildResult[Coord]:
        """
        # Action:
        1.  coord_validator runs integrity checks on the target param.
        2.  scalar_service runs integrity checks on the scalar param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If target and scalar params are valid:
                new_row, new_colum = target.row * scalar.value, target.column * scalar.value
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   target (Coord):
            *   scalar (Scalar):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    coord_validator
                    scalar_service
            *   coord_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.multiply_coord_by_scalar"
        
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
        """
        # Action:
        1.  vector_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_coord(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # Parameters:
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   vector_service sends any validation exceptions back to the caller.
            *   coord_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.convert_vector_to_coord"
        
        try:
            vector_validation = self._vector_service.validate_as_vector(candidate=vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            return self._coord_builder.build(row=vector.y, column=vector.x)
        except Exception as ex:
            return BuildResult.failure(ex)
        
        
    @LoggingLevelRouter.monitor
    def coord_search_by_row(self, collection: List[Coord], row: int) -> BuildResult[List[Coord]]:
        """Search a collection of coords by the row."""
        method = "CoordService.coord_search_by_row"
        return self._search_service.search_by_row(collection=collection, row=row)
    
    @LoggingLevelRouter.monitor
    def coord_search_by_column(self, collection: List[Coord], column: int) -> BuildResult[List[Coord]]:
        """Search a collection of coords by the column."""
        method = "CoordService.coord_search_by_column"
        return self._search_service.search_by_column(collection=collection, column=column)
    
    
    def coord_search_by_coord(self, collection: List[Coord], coord: Coord) -> BuildResult[List[Coord]]:
        """Search a collection of coords for a specific coor.d"""
        method = "CoordService.coord_search_by_coord"
        return self._search_service.search_by_coord(collection=collection, coord=coord)
        
    