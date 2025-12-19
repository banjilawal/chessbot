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
from chess.system import BuildResult, EntityService, NotNegativeNumberValidator, id_emitter
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
    SERVICE_NAME = "CoordService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: CoordBuilder = CoordBuilder(),
            validator: CoordValidator = CoordValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
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
    
    def add_vector_to_coord(
            self,
            coord: Coord,
            vector: Vector,
            vector_service: VectorService = VectorService(),
            number_validator: NotNegativeNumberValidator = NotNegativeNumberValidator(),
    ) -> BuildResult[Coord]:
        """
        # Action:
        1.  Certify the vector argument with vector_service.
        2.  Certify the coord argument with the service's validator.
        3.  Get the new row and column using the expression
                    new_row, new_colum = coord.row + vector.y, coord.column + vector.x
        5.  Using the service's CoordBuilder instance create and return the new Coord.

        # Parameters:
            *   coord(Coord)
            *   vector (Vector)
            *   vector_service (VectorService)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   CoordServiceException
        """
        method = "CoordService.add_vector_to_coord"
        try:
            # Certify the coord param
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            # Certify the vector param.
            vector_validation = vector_service.validator.validate(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            
            # when params are certified return the BuildResult.
            return self.builder.build(
                row=(coord.row + vector.y), column=(coord.column + vector.x), validator=self.validator
            )
        # Finally, if there is an unhandled exception Wrap a CoordServiceException around it then return the
        # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, message= f"{method}: {CoordServiceException.DEFAULT_MESSAGE}")
            )
      
    def multiply_coord_by_scalar(
            self,
            coord: Coord,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
    ) -> BuildResult[Coord]:
        """
        # Action:
        1.  Certify the vector argument with vector_service.
        2.  Certify the coord argument with the service's validator.
        3.  Get the new row and column using the expression
                    new_row, new_colum = coord.row * scalar.value, coord.column + scalar.value
        5.  Using the service's CoordBuilder instance create and return the new Coord.

        # Parameters:
            *   coord(Coord)
            *   scalar (Scalar)
            *   scalar_service (ScalarService)
            *   number_validator (NotNegativeNumberValidator)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   CoordServiceException
        """
        method = "CoordService.multiply_coord_by_scalar"
        try:
            # Certify the coord param
            coord_validation = self._validator.validate(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            # Certify the scalar param
            scalar_validation = scalar_service.validator.validate(candidate=scalar)
            if scalar_validation.is_failure:
                return BuildResult.failure(scalar_validation.exception)
            
            # when params are certified return the BuildResult.
            return self._builder.build(
                row=(coord.y * scalar.value), column=(coord.x * scalar.value), validator=self.validator
            )
            # Finally, if there is an unhandled exception Wrap a CoordServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, message=f"{method}: {CoordServiceException.DEFAULT_MESSAGE}")
            )
        
        
    def convert_vector_to_coord(
            self,
            vector: Vector,
            vector_service: VectorService = VectorService()
    ) -> BuildResult[Coord]:
        """
        # Action:
        1.  vector_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_coord(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # Parameters:
            *   vector (Vector)
            *   vector_service (VectorService)

        # Returns:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        Raises:
            *   CoordServiceException
        """
        method = "CoordService.convert_vector_to_coord"
        try:
            # Certify the vector param
            vector_validation = vector_service.validator.validate(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            # After the vector is certified return the BuildResult.
            return self._builder.build(row=vector.y, column=vector.x, validator=self.validator
                                       )
            # Finally, if there is an unhandled exception Wrap a CoordServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, message=f"{method}: {CoordServiceException.DEFAULT_MESSAGE}")
            )
    
