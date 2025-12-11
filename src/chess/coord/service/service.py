# src/chess/coord/service/service.py

"""
Module: chess.coord.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import cast


from chess.scalar import Scalar, ScalarService
from chess.vector import Vector, VectorService
from chess.system import BuildResult, EntityService, id_emitter
from chess.coord import Coord, CoordBuilder, CoordServiceException, CoordValidator


class CoordService(EntityService[Coord]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Coord State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Coord state by providing single entry and exit points to Coord
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   CoordService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "CoordService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: CoordBuilder = CoordBuilder(),
            validator: CoordValidator = CoordValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (CoordFactory)
            *   validator (CoordValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def builder(self) -> CoordBuilder:
        """get CoordBuilder"""
        return cast(CoordBuilder, self.entity_builder)
    
    @property
    def validator(self) -> CoordValidator:
        """get CoordValidator"""
        return cast(CoordValidator, self.entity_validator)
    
    def add_vector_to_coord(self, coord: Coord, vector: Vector, vector_service: VectorService = VectorService()) -> BuildResult[Coord]:
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
            *   CoordServiceException
        """
        method = "CoordService.add_vector_to_coord"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = vector_service.validator.validate(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            
            return self._builder.build(
                row=(coord.row + vector.y),
                column=(coord.column + vector.x),
                validator=self._validator
            )
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
      
    def multiply_coord_by_scalar(self, coord: Coord, scalar: Scalar, scalar_service: ScalarService = ScalarService()) -> BuildResult[Coord]:
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
            *   CoordServiceException
        """
        method = "CoordService.multiply_coord_by_scalar"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            
            scalar_validation = scalar_service.alidator.validate(candidate=scalar)
            if scalar_validation.is_failure:
                return BuildResult.failure(scalar_validation.exception)
            
            return self._builder.build(
                row=(coord.y * scalar.value),
                column=(coord.x * scalar.value),
                validator=self._validator
            )
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        
    def convert_vector_to_coord(self, vector: Vector, vector_service: VectorService = VectorService()) -> BuildResult[Coord]:
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
            *   CoordServiceException
        """
        method = "CoordService.convert_vector_to_coord"
        
        try:
            vector_validation = vector_service.validator.validate(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            
            return self._builder.build(
                row=vector.y,
                column=vector.x,
                validator=self._validator
            )
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    def convert_coord_to_vector(self, coord: Coord, vector_service: VectorService = VectorService()) -> BuildResult[Vector]:
        """
        # Action:
        1.  self._validator runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run vector_service.buil to ensure the computed values produce a
            safe vector instance.

        # Parameters:
            *   coord (Coord):

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   CoordServiceException
        """
        method = "CoordService.convert_coord_to_vector"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            return vector_service.builder.build(
                x=coord.column,
                y=coord.row,
                validator=vector_service.validator
            )
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )