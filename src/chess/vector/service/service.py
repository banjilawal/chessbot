# src/chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.coord import Coord, CoordService
from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, LoggingLevelRouter, EntityService, id_emitter
from chess.vector import Vector, VectorBuilder, VectorServiceException, VectorValidator


class VectorService(EntityService[Vector]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Vector State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Vector state by providing single entry and exit points to Vector
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   VectorService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "VectorService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: VectorBuilder = VectorBuilder(),
            validator: VectorValidator = VectorValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (VectorBuilder)
            *   number_bounds_validator (VectorValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> VectorBuilder:
        """get VectorBuilder"""
        return cast(VectorBuilder, self.entity_builder)
    
    @property
    def validator(self) -> VectorValidator:
        """get VectorValidator"""
        return cast(VectorValidator, self.entity_validator)
    
    
    @LoggingLevelRouter.monitor
    def multiply_vector_by_scalar(
            self,
            vector: Vector,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService()
    ) -> BuildResult[Vector]:
        """
        # Action:
        1.  Certify the scalar argument with scalar_service.
        2.  Certify the vector argument with the service's number_bounds_validator.
        3.  Get the new x and y components using the expression
                    x, new_colum = vector.x * scalar.value, vector.y * scalar.value
        5.  Using the service's VectordBuilder instance create and return the new Vector.

        # Parameters:
            *   vector(Vector)
            *   scalar (Scalar)
            *   scalar_service (ScalarService)

        # Returns:
        BuildResult[Vector] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        Raises:
            *   VectorServiceException
        """
        method = "VectorService.multiply_vector_by_scalar"
        try:
            # Certify the vector param
            vector_validation = self._validator.validate(vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            # Certify the scalar param
            scalar_validation = scalar_service.validator.validate(candidate=scalar)
            if scalar_validation.is_failure:
                return BuildResult.failure(scalar_validation.exception)
            
            # when params are certified return the BuildResult.
            return self.builder.build(
                x=(vector.x * scalar.value), y=(vector.y * scalar.value), validator=self.validator
            )
            # Finally, if there is an unhandled exception Wrap a VectorServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                VectorServiceException(ex=ex, message=f"{method}: {VectorServiceException.DEFAULT_MESSAGE}")
            )
    
    @LoggingLevelRouter.monitor
    def convert_coord_to_vector(
            self,
            coord: Coord,
            coord_service: CoordService = CoordService(),
    ) -> BuildResult[Vector]:
        """
        # Action:
        1.  coord_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_coord(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # Parameters:
            *   coord (Coord)
            *   coord_service (CoordService)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   VectorServiceException
        """
        method = "vectorService.convert_coord_to_vector"
        try:
            # Certify the coord param
            coord_validation = coord_service.validator.validate(candidate=coord)
            if coord_validation.is_failure():
                return BuildResult.failure(coord_validation.exception)
            # After the coord is certified return the BuildResult.
            return self.builder.build(x=coord.column, y=coord.row)
            
            # Finally, if there is an unhandled exception Wrap a VectorServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                VectorServiceException(ex=ex, message=f"{method}: {VectorServiceException.DEFAULT_MESSAGE}")
            )