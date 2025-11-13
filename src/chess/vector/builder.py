# chess/vector/builder.py

"""
Module: chess.vector.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from typing import cast

from chess.system import Builder, BuildResult, KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, VectorBuildFailedException, NullXComponentException, NullYComponentException,
    VectorBelowBoundsException, VectorAboveBoundsException
)

class VectorBuilder(Builder[Vector]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
    1. Process and validate parameters for creating Vector instances.
    2. Create new Vector objects if parameters meet specifications.
    2. Report errors and return BuildResult with error details.

    # PROVIDES:
      BuildResult[Vector] containing either:
            - On success: Vector in payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor()
    def build(cls, x: int, y: int) -> BuildResult[Vector]:
        """
        ACTION:
        Create a Vector object if the parameters are not null and their values are within
        the systems bounds.

        PARAMETERS:
            * x (int): value in the x-plane
            * y (int): value in the y-plane

        # Returns:
        BuildResult[Scalar] containing either:
            - On success: Scalar in payload.
            - On failure: Exception.

        RAISES:
            * NullXComponentException
            * NullYComponentException
            * VectorBelowBoundsException
            * VectorAboveBoundsException
        """
        method = "VectorBuilder.build"

        try:
            build_x_result = cls.process_x_component(x)
            if build_x_result.is_failure():
                return BuildResult.failure(build_x_result.exception)
            
            build_y_result = cls.process_y_component(y)
            if build_y_result.is_failure():
                return BuildResult.failure(build_y_result.exception)
            
            x = build_x_result.payload
            y = build_y_result.payload

            return BuildResult.success(
                payload=Vector(x=build_x_result.payload, y=build_y_result.payload)
            )

        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def process_x_component(cls, x_component: int) -> BuildResult[int]:
        """
        ACTION:
        Build the x component of a Vector object.

        PARAMETERS:
            * x_component (int): The object to validate.

        # Returns:
          BuildResult[int] containing either:
                - On success: int in payload.
                - On failure: Exception.

        RAISES:
            * TypeError
            * NullXComponentException
            * VectorBelowBoundsException
            * VectorAboveBoundsException
            * InvalidVectorException
        """
        method = "VectorValidator.process_x_component"
        
        try:
            if x_component is None:
                return BuildResult.failure(
                    NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(x_component, int):
                return BuildResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(x_component).__name__} instead.")
                )
            x = cast(int, x_component)
            
            if x < -KNIGHT_STEP_SIZE:
                return BuildResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if x >= KNIGHT_STEP_SIZE:
                return BuildResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return BuildResult.success(payload=x)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def process_y_component(cls, y_component: int) -> BuildResult[int]:
        """
        ACTION:
        Build the y component of a Vector object.

        PARAMETERS:
            * y_component (int):

        # Returns:
          BuildResult[int] containing either:
                - On success: int in payload.
                - On failure: Exception.

        RAISES:
            * TypeError
            * NullYComponentException
            * VectorBelowBoundsException
            * VectorAboveBoundsException
            * InvalidVectorException
        """
        method = "VectorValidator._validate_y_component"
        
        try:
            if y_component is None:
                return BuildResult.failure(
                    NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(y_component, int):
                return BuildResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(y_component).__name__} instead.")
                )
            y = cast(int, y_component)
            
            if y < -KNIGHT_STEP_SIZE:
                return BuildResult.failure(
                    VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if y >= KNIGHT_STEP_SIZE:
                return BuildResult.failure(
                    VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return BuildResult.success(payload=y)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )