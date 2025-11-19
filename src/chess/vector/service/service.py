# src/chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import Any

from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, LoggingLevelRouter, ValidationResult
from chess.vector import Vector, VectorBuildFailedException, VectorBuilder, VectorValidator


class VectorService:
    """
    # ROLE: Service, Data Protect

    # RESPONSIBILITIES:
    1.  Manages integrity lifecycle of Vector objects.
    2.  Compute dot product of Scalar and Vector objects.

    # PROVIDES:
        * VectorBuilder
        * VectorValidator
        * Vector exceptions

    # ATTRIBUTES:
        *   vector_builder (type[VectorBuilder]): Builds new Vector instances that meet
            the application's safety contract.
        *   vector_validator (type[VectorValidator]): Ensures an existing Vector will not raise an
            exception when used by a client.
        *   scalar_service (type[ScalarService]): Provides scalar product functionality.
    """
    _vector_builder: type[VectorBuilder]
    _vector_validator: type[VectorValidator]
    _scalar_service: ScalarService
    
    def __init__(
            self,
            vector_builder: type[VectorBuilder] = VectorBuilder,
            vector_validator: type[VectorValidator] = VectorValidator,
            scalar_service: ScalarService = ScalarService()
    ):
        self._vector_builder = vector_builder
        self._vector_validator = vector_validator
        self._scalar_service = scalar_service
    
    
    @LoggingLevelRouter.monitor
    def build_vector(self, x: int, y: int) -> BuildResult[Vector]:
        """
        # Action:
        VectorService directs vector_builder to run the build process with the inputs.

        # Parameters:
            *   x (int):
            *   y (int):

        # Returns:
        BuildResult[Vector] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   vector_builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "VectorService.build_vector"
        return self._vector_builder.build(x=x, y=y)
    
    
    @LoggingLevelRouter.monitor
    def validate_as_vector(self, candidate: Any) -> ValidationResult[Vector]:
        """
        # Action:
        VectorService directs vector_validator to run the verification process on the candidate.

        # Parameters:
            *   candidate (Any):

        # Returns:
        ValidationResult[Vector] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here.
            *   vector_validator sends any validation exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "VectorService.validate_as_vector"
        return self._vector_validator.validate(candidate)
    
    
    @LoggingLevelRouter.monitor
    def multiply_vector_by_scalar(self, vector: Vector, scalar: Scalar) -> BuildResult[Vector]:
        """
        # Action:
        1.  vector_validator runs integrity checks on the vector param.
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
        method = "VectorService.multiply_by_scalar"
        
        try:
            scalar_validation = self._scalar_service.validate_as_scalar(scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            vector_validation = self._vector_validator.validate(vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            x_component = vector.x * scalar.value
            y_component = vector.y * scalar.value
            
            return self._vector_builder.build(x=x_component, y=y_component)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )