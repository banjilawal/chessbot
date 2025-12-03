# src/chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import cast

from chess.scalar import Scalar, ScalarIntegrityService
from chess.system import BuildResult, LoggingLevelRouter, IntegrityService
from chess.vector import Vector, VectorBuildFailedException, VectorBuilder, VectorValidator


class VectorIntegrityService(IntegrityService[Vector]):
    """
    # ROLE: IntegrityService, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Vector objects, VectoValidator and VectorBuilder.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects Vector objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   Vector building
        *   Vector validation
        *   Vector exceptions
        *   Dot Product functionality

    # ATTRIBUTES:
        *   builder (VectorBuilder)
        *   validator (VectorValidator)
        *   scalar_service (ScalarIntegrityService)
    """
    SERVICE_NAME = "VectorIntegrityService"
    
    _scalar_service: ScalarIntegrityService
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: VectorBuilder = VectorBuilder(),
            validator: VectorValidator = VectorValidator(),
            scalar_service: ScalarIntegrityService = ScalarIntegrityService()
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._scalar_service = scalar_service
    
    
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, self.item_validator)
    
    
    @property
    def builder(self) -> VectorBuilder:
        return cast(VectorBuilder, self.item_builder)
    
    @LoggingLevelRouter.monitor
    def build(self, x: int, y: int) -> BuildResult[Vector]:
        """
        # Action:
        VectorIntegrityService directs builder to run the builder process with the inputs.

        # Parameters:
            *   x (int):
            *   y (int):

        # Returns:
        BuildResult[Vector] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   builder sends any builder exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "VectorIntegrityService.build_vector"
        return self._item_builder.build(x=x, y=y, validator=self._item_validator)
    
    
    @LoggingLevelRouter.monitor
    def multiply_vector_by_scalar(self, vector: Vector, scalar: Scalar) -> BuildResult[Vector]:
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
        method = "VectorIntegrityService.multiply_vector_by_scalar"
        
        try:
            scalar_validation = self._scalar_service.item_validator.validate(scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            vector_validation = self._item_validator.validate(vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            return self._item_builder.build(
                x=(vector.x * scalar.value),
                y=(vector.y * scalar.value),
                validator=self._item_validator
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