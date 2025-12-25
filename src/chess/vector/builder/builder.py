# src/chess/vector/builder/builder.py

"""
Module: chess.vector.builder.__init__
Author: Banji Lawal
Created: 2025-09083
version: 1.0.0
"""

from typing import Any, cast

from chess.system import Builder, BuildResult, LoggingLevelRouter
from chess.vector import Vector, VectorBuildFailedException,VectorValidator


class VectorBuilder(Builder[Vector]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce Vector instances whose integrity is guaranteed at creation.
     2.  Manage construction of Vector instances that can be used safely by the client.
     3.  Ensure params for Vector creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   VectorBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    @LoggingLevelRouter.monitor
    def build(
            self,
            x: int,
            y: int,
            validator: VectorValidator = VectorValidator(),
    ) -> BuildResult[Vector]:
        """
        # ACTION:
        1.  Use validator to certify x is safe.
        2.  Use validator to certify y is safe.
        3.  If either validation fails return their exception inside a BuildResult.
        4.  Otherwise, return a BuildResult containing a Vector.

        # PARAMETERS:
            *   x (int)
            *   y (int)
            *   validator (VectorValidator)
            
        # Returns:
        BuildResult[Vector] containing either:
            - On success: V in the payload.
            - On failure: Exception.

        RAISES:
            *   VectorBuildFailedException
        """
        method = "VectorBuilder.builder"
        
        try:
            x_component_validation = validator.validate_x_component(x)
            if x_component_validation.is_failure():
                return BuildResult.failure(x_component_validation.exception)
            
            y_component_validation = validator.validate_y_component(y)
            if y_component_validation.is_failure():
                return BuildResult.failure(y_component_validation.exception)
            
            x = cast(int, x_component_validation.payload)
            y = cast(int, y_component_validation.payload)
            
            return BuildResult.success(payload=Vector(x=x, y=y))
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    ex=ex,
                    message=f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}",
                )
            )
