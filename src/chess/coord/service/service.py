# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import Any, List

from chess.scalar import Scalar, ScalarService
from chess.vector import Vector, VectorService
from chess.system import BuildResult, LoggingLevelRouter, Result, SearchResult, Service
from chess.coord import (
    AddingDuplicateCoordException, Coord, CoordBuilder, CoordServiceException, CoordValidator,
    CoordSearchService, RemovingNonExistentCoordException
)


class CoordService(Service[Coord]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Square, VectoValidator and SquareBuilder objects.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects Square objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator

    # ATTRIBUTES:
        *   builder (type[SquareBuilder]):
        *   validator (type[SquareValidator]):
        *   coord_service (CoordService)
        *   identity_service (IdentityService)
    """
    """
    # ROLE: Service, Data Protraction

    # RESPONSIBILITIES:
    1.  Manages integrity lifecycle of Coord objects.
    2.  Vector addition and scalar multiplication of Coord objects.
    3.  Calculate distance between two Coords.
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for CoordStackValidator and CoordStackBuilder.
    2.  Protects CoordStack objects from direct manipulation.
    3.  Extends behavior and functionality of CoordStack objects.
    4.  Public facing API for CoordStack modules.
    5.  Vector addition
    6.  Scalar multiplication
    
    # PROVIDES:
        *   CoordBuilding
        *   CoordValidation
        *   Scalar multiplication
        *   Vector addition


    # ATTRIBUTES:
        *   builder (type[CoordBuilder])
        
        *   validator (type[CoordValidator])
        
        *   scalar_service (type[ScalarService):
        
        *   vector_service (type[VectorService])
    """
    SERVICE_NAME = "CoordService"
    
    id: int
    name: str
    _coords: List[Coord] = []
    _builder: type[CoordBuilder]
    _validator: type[CoordValidator]
    _scalar_service: ScalarService
    _vector_service: VectorService
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: type[CoordBuilder] = CoordBuilder,
            validator: type[CoordValidator] = CoordValidator,
            scalar_service: ScalarService = ScalarService(),
            vector_service: VectorService = VectorService(),
    ):
        super().__init__(id=id, name=name)
        self._coord_builder = builder
        self._validator = validator
        self._scalar_service = scalar_service
        self._vector_service = vector_service
        
        self._coords = []
        
    
    @property
    def validator(self) -> type[CoordValidator]:
        """
        CoordValidator is the single-source-of truth for certifying the safety of
        Coord instances, their organic row and column attributes. It makes sense
        providing direct access here and letting validator return its Validation
        result directly to the caller.
        """
        return self._validator
    
    
    # @property
    # def coords(self) -> List[Coord]:
    #     return self._coords
    
    
    def add_coord(self, coord: Coord) -> Result[Coord]:
        method = "CoordService.add_coord"
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return Result.failure(coord_validation.exception)
            if coord in self._squares:
                return Result.failure(
                    AddingDuplicateCoordException(
                        f"{method}: {AddingDuplicateCoordException.DEFAULT_MESSAGE}"
                    )
                )
            self._squares.append(coord)
            return Result.success(coord)
        except Exception as ex:
            return Result.failure(
                CoordServiceException(
                    f"{method}: ex=ex, message={CoordServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def remove_coord(self, coord: Coord) -> Result[Coord]:
        method = "CoordService.remove_coord"
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return Result.failure(coord_validation.exception)
            if coord not in  self._coords:
                return Result.failure(
                    RemovingNonExistentCoordException(
                        f"{method}: {RemovingNonExistentCoordException.DEFAULT_MESSAGE}"
                    )
                )
            coord = self._coords.remove(coord)
            return Result.success(coord)
        except Exception as ex:
            return Result.failure(
                CoordServiceException(
                    f"{method}: ex=ex, message={CoordServiceException.DEFAULT_MESSAGE}"
                )
            )
        
        
    def find_coord(self, coord: Coord) -> SearchResult[[Coord]]:
        method = "CoordService.find_coord"
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return SearchResult.failure(coord_validation.exception)
            
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
                CoordServiceException(
                    f"{method}: ex=ex, message={CoordServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_coord_by_row(self, row: int) -> SearchResult[[Coord]]:
        method = "CoordService.find_coord_by_row"
        try:
            row_validation = self._validator.validate_row(row)
            
            matches = [coord for coord in self._coords if coord.row == row]
            if len(matches) == 0:
                return SearchResult.empty()
            
            elif len(matches) > 1:
                return SearchResult.success(payload=matches)
            
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
                CoordServiceException(
                    f"{method}: ex=ex, message={CoordServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    
    def find_coord_by_colum(self, column: int) -> SearchResult[[Coord]]:
        method = "CoordService.find_coord_by_row"
        try:
            row_validation = self._validator.validate_column(column)
            
            matches = [coord for coord in self._coords if coord.column == column]
            if len(matches) == 0:
                return SearchResult.empty()
            
            elif len(matches) > 1:
                return SearchResult.success(payload=matches)
            
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
                CoordServiceException(
                    f"{method}: ex=ex, message={CoordServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    # def validate_as_coord(self, candidate: Any) -> ValidationResult[Coord]:
    #     """
    #     # Action:
    #     CoordService directs validator to run the verification process on the candidate.
    #
    #     # Parameters:
    #         *   row (int):
    #         *   column (int):
    #
    #     # Returns:
    #     BuildResult[Coord] containing either:
    #         - On success: Coord in the payload.
    #         - On failure: Exception.
    #
    #     Raises:
    #         *   None are raised here.
    #         *   validator sends any validation exceptions back to the caller.
    #         *   The caller is responsible for safely handling any exceptions it receives.
    #     """
    #     return self._validator.validate(candidate=candidate)
    
    
    def build_coord(self, row: int, column: int) -> BuildResult[Coord]:
        """
        # Action:
        CoordService directs builder to run the builder process with the inputs.

        # Parameters:
            *   row (int):
            *   column (int):
            
        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   builder sends any builder exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        return self._coord_builder.build(row=row, column=column)
    
    
    def add_vector_to_coord(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  validator runs integrity checks on the square param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If square and vector params are valid:
                new_row, new_colum = square.row + vector.y, square.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   square(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    vector_service
            *   builder sends any builder exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.add_vector_to_coord"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
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
    
    def cross_product(self, coord: Coord, vector: Vector) -> BuildResult[Coord]:
        """
        # Action:
        1.  validator runs integrity checks on the square param.
        2.  vector_service runs integrity checks on the vector param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If square and vector params are valid:
                new_row, new_colum = square.row + vector.y, square.column + vector.x
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   square(Coord):
            *   vector (Vector):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    vector_service
            *   builder sends any builder exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.dot_product"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
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
        1.  validator runs integrity checks on the square param.
        2.  scalar_service runs integrity checks on the scalar param.
        3.  If any checks raise an exception return it in the BuildResult.
        4.  If square and scalar params are valid:
                new_row, new_colum = square.row * scalar.value, square.column * scalar.value
        5.  Run build_coord(new_row, new_column) to ensure the computed values produce a safe Coord instance.

        # Parameters:
            *   square (Coord):
            *   scalar (Scalar):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   Any validation exceptions that occur are sent to the caller by either
                    validator
                    scalar_service
            *   builder sends any builder exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "CoordService.multiply_coord_by_scalar"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
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
            *   builder sends any builder exceptions back to the caller.
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
    