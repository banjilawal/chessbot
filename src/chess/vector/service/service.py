# src/chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import cast

from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, LoggingLevelRouter, EntityService
from chess.vector import Vector, VectorBuildFailedException, VectorBuilder, VectorValidator


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
    DEFAULT_NAME = "VectorService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: VectorBuilder = VectorBuilder(),
            validator: VectorValidator = VectorValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (VectorBuilder)
            *   validator (VectorValidator)

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
    def multiply_vector_by_scalar(self, vector: Vector, scalar: Scalar, scalar_service: ScalarService = ScalarService()) -> BuildResult[Vector]:
        """
        # Action:
        1.  validator runs integrity checks on the vector param.
        2.  scalar_service runs integrity checks on the scalar param.
        3.  If any checks raise an exception return to called in a BuildResult.
        4.  If vector and scalar params are valid:
                new_x, new_y = vector.x * scalar.value, vector.y * scalar.value
        5.  Run build_vector(new_x, new_y) to ensure the computed values produce a
            safe Vector instance.
        
        # Parameters:
            *   vector (Vector):
            *   scalar (Scalar):
        
        # Returns:
        BuildResult[Vector] containing either:
            - On success: int in the payload.
            - On failure: Exception.
        
        Raises:
            VectorBuildFailedException
        """
        method = "VectorService.multiply_vector_by_scalar"
        
        try:
            scalar_validation = self._scalar_service.validator.validate(scalar)
            if scalar_validation.is_failure:
                return BuildResult.failure(scalar_validation.exception)
            
            vector_validation = self._validator.validate(vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            
            return self._builder.build(
                x=(vector.x * scalar.value),
                y=(vector.y * scalar.value),
                validator=self._validator
            )
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{VectorBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )