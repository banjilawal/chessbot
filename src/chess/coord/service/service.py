# src/chess/coord/service/service.py

"""
Module: chess.coord.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import BuildResult, EntityService, id_emitter
from chess.scalar import Scalar, ScalarService
from chess.vector import Vector, VectorService
from chess.coord import Coord, CoordBuilder, CoordServiceException, CoordValidator


class CoordService(EntityService[Coord]):
    """
    # RESPONSIBILITIES:

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator
        *   Coord Data EntityService
        *

    # ATTRIBUTES:
        *   builder (type[SquareBuilder]):
        *   validator (type[SquareValidator]):
    """
    """
    # ROLE: EntityService, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  An API for managing the integrity lifecycle of Coord objects through CoordBuilder and CoordValidator.
    2.  Protects Coord instances from direct access to assure high reliability and consistency from a single
        source of truth.Assure reliability and consistency by protecting Coord objects from direct access.direct access to Coord objects.
    3.  Vector addition
    4.  Scalar multiplication
    5.  Converting Vectors to Coords and vice versa.
    
    # PROVIDES:
        *   CoordBuilder
        *   CoordValidator
        *   VectorService
        *   ScalarService

    # ATTRIBUTES:
        *   builder (type[CoordBuilder])
        *   validator (type[CoordValidator])
        *   scalar_service (type[ScalarService):
        *   vector_service (type[VectorService])
    """
    SERVICE_NAME = "CoordService"
    
    _id: int
    _name: str
    _item_builder: CoordBuilder
    _item_validator: CoordValidator
    _scalar_service: ScalarService
    _vector_service: VectorService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: CoordBuilder = CoordBuilder(),
            validator: CoordValidator = CoordValidator(),
            scalar_service: ScalarService = ScalarService(),
            vector_service: VectorService = VectorService(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._scalar_service = scalar_service
        self._vector_service = vector_service
      
    
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
            *   CoordServiceException
        """
        method = "CoordService.add_vector_to_coord"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            vector_validation = self._vector_service.item_validator.validate(candidate=vector)
            if vector_validation.is_failure():
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
            *   CoordServiceException
        """
        method = "CoordService.multiply_coord_by_scalar"
        
        try:
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            
            scalar_validation = self._scalar_service.item_validator.validate(candidate=scalar)
            if scalar_validation.is_failure():
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
            *   CoordServiceException
        """
        method = "CoordService.convert_vector_to_coord"
        
        try:
            vector_validation = self._vector_service.item_validator.validate(candidate=vector)
            if vector_validation.is_failure():
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
    
    def convert_coord_to_vector(self, coord: Coord) -> BuildResult[Vector]:
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
            
            return self._vector_service.build(
                x=coord.colum,
                y=coord.row,
                validator=self._vector_service.item_validator
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