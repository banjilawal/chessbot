# chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, LoggingLevelRouter, ValidationResult
from chess.vector import Vector, VectorBuilder, VectorValidator


class VectorService:
    """
    # ROLE: Service

    # RESPONSIBILITIES:
    An interface that provides access to a Vector object's state and methods without
    exposing the Vector directly.

    # PROVIDES:
        * VectorBuilder
        * VectorValidator
        * Vector exceptions

    # ATTRIBUTES:
        * vector_builder (type[VectorBuilder]): Builds new Vector instances that meet
            the application's safety contract.
        * vector_validator (type[VectorValidator]): Ensures an existing Vector will not raise an
            exception when used by a client.
        * scalar_service (type[ScalarService]): Provides scalar product functionality.
    """
    
    _vector_builder: type[VectorBuilder]
    _vector_validator: type[VectorValidator]
    _scalar_service: type[ScalarService]
    
    def __init__(
            self,
            vector_builder: type[VectorBuilder] = VectorBuilder,
            vector_validator: type[VectorValidator] = VectorValidator,
            scalar_service: type[ScalarService] = ScalarService
    ):
        self._vector_builder = vector_builder
        self._vector_validator = vector_validator
        self._scalar_service = scalar_service
    
    @LoggingLevelRouter.monitor
    def build_vector(self, x: int, y: int) -> BuildResult[Vector]:
        """
        # Action:
        Build a Vector

        # Parameters:
            * x (int):
            * y (int):

        # Returns:
        BuildResult[Vector] containing either:
            - On success: Vector in payload.
            - On failure: Exception.

        Raises:
        None
        """
        method = "VectorService.build_vector"
        return self._vector_builder.build(x=x, y=y)
    
    @LoggingLevelRouter.monitor
    def validate_as_vector(self, candidate: Any) -> ValidationResult[Vector]:
        """
        # Action:
        Validate an object is a Vector

        # Parameters:
            * candidate (Any):

        # Returns:
        ValidationResult[Vector] containing either:
            - On success: int in payload.
            - On failure: Exception.

        Raises:
        None
        """
        method = "VectorService.validate_as_vector"
        
        return self._vector_validator.validate(candidate)
    
    @LoggingLevelRouter.monitor
    def scalar_product(self, vector: Vector, scalar: Scalar) -> BuildResult[Vector]:
        """
        # Action:
        Multiply a Vector by a scalar.
        
        # Parameters:
            * scalar (Scalar):
            * vector (Vector):
        
        # Returns:
        ValidationResult[Vector] containing either:
            - On success: int in payload.
            - On failure: Exception.
        
        Raises:
        None
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
        
        except Exception as e:
            return BuildResult.failure(e)


