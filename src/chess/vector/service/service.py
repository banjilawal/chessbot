# src/chess/vector/service.py

"""
Module: chess.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""


from chess.scalar import Scalar, ScalarService
from chess.system import BuildResult, LoggingLevelRouter, Service
from chess.vector import Vector, VectorBuildFailedException, VectorBuilder, VectorValidator


class VectorService(Service):
    """
    # ROLE: Service, Encapsulation, API layer.

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
        *   builder (type[VectorBuilder]):       Builds new Vector instances that meet
                                                        the application's safety contract.
                                                        
        *   validator (type[VectorValidator]):   Ensures an existing Vector will not raise an
                                                        exception when used by a client.
                                                        
        *   scalar_service (type[ScalarService]):       Provides scalar product functionality.
    """
    SERVICE_NAME = "VectorService"
    
    _builder: type[VectorBuilder]
    _validator: VectorValidator
    _scalar_service: ScalarService
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            builder: type[VectorBuilder] = VectorBuilder,
            validator: VectorValidator = VectorValidator,
            scalar_service: ScalarService = ScalarService()
    ):
        self._builder = builder
        self._validator = validator
        self._scalar_service = scalar_service
    
    
    @property
    def validator(self) -> VectorValidator:
        return self._validator
    
    @LoggingLevelRouter.monitor
    def build_vector(self, x: int, y: int) -> BuildResult[Vector]:
        """
        # Action:
        VectorService directs builder to run the build process with the inputs.

        # Parameters:
            *   x (int):
            *   y (int):

        # Returns:
        BuildResult[Vector] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        Raises:
            *   None are raised here
            *   builder sends any build exceptions back to the caller.
            *   The caller is responsible for safely handling any exceptions it receives.
        """
        method = "VectorService.build_vector"
        return self._builder.build(x=x, y=y)
    
    
    # @LoggingLevelRouter.monitor
    # def validate_as_vector(self, candidate: Any) -> ValidationResult[Vector]:
    #     """
    #     # Action:
    #     VectorService directs validator to run the verification process on the candidate.
    #
    #     # Parameters:
    #         *   candidate (Any):
    #
    #     # Returns:
    #     ValidationResult[Vector] containing either:
    #         - On success: int in the payload.
    #         - On failure: Exception.
    #
    #     Raises:
    #         *   None are raised here.
    #         *   validator sends any validation exceptions back to the caller.
    #         *   The caller is responsible for safely handling any exceptions it receives.
    #     """
    #     method = "VectorService.validate_as_vector"
    #     return self._validator.validate(candidate)
    
    
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
        method = "VectorService.multiply_by_scalar"
        
        try:
            scalar_validation = self._scalar_service.validator.validate(scalar)
            if scalar_validation.is_failure():
                return BuildResult.failure(scalar_validation.exception)
            
            vector_validation = self._validator.validate(vector)
            if vector_validation.is_failure():
                return BuildResult.failure(vector_validation.exception)
            
            x_component = vector.x * scalar.value
            y_component = vector.y * scalar.value
            
            return self._builder.build(x=x_component, y=y_component)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    ex=ex,
                    message=f"{method}: "
                            f"{VectorBuildFailedException.DEFAULT_MESSAGE}"
                )
            )