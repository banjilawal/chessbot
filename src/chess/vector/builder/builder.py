# src/chess/vector/builder/builder.py

"""
Module: chess.vector.builder.__init__
Author: Banji Lawal
Created: 2025-09083
version: 1.0.0
"""

from typing import Any, cast

from chess.system import Builder, BuildResult, LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, VectorBuildFailedException, NullXComponentException, NullYComponentException,
    VectorBelowBoundsException, VectorAboveBoundsException, VectorValidator
)


class VectorBuilder(Builder[Vector]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Coord instances whose integrity is always guaranteed. If any attributes do not pass their integrity checks,
    send an exception instead.

    # PROVIDES:
    BuildResult[Vector] containing either:
        - On success: Vector in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
        * vector_validator (VectorValidator)
    """
    _vector_validator: VectorValidator
    
    def __init__(self, ) -> None:
    

    @LoggingLevelRouter.monitor
    def build(
            self,
            x: int,
            y: int,
            vector_validator: VectorValidator = VectorValidator(),
    ) -> BuildResult[Vector]:
        """
        # ACTION:
        1.  Check x is:
            *   an INT
            *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE inclusive.
        2.  Check y is:
            *   an INT
            *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE inclusive.
        3.  If any check fails, return the exception inside a BuildResult.
        2.  When all checks create a new Vector and return in a BuildResult

        # PARAMETERS:
            *   x (int): value in the x-plane
            *   y (int): value in the y-plane

        # Returns:
        BuildResult[Vector] containing either:
            - On success: V in the payload.
            - On failure: Exception.

        RAISES:
            *   VectorBuildFailedException
        """
        method = "VectorBuilder.builder"
        
        try:
            x_component_validation = cls._validate_x_component(x)
            if x_component_validation.is_failure():
                return BuildResult.failure(x_component_validation.exception)
            
            y_component_validation = cls._validate_y_component(y)
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_x_component(cls, candidate: Any) -> BuildResult[int]:
        """
        # ACTION:
        1.  Test if candidate is:
                *   not validation
                *   is an int
                *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE] exclusive.
        2.  If any check fails return its exception inside a BuildResult.
        3.  Otherwise cast candidate to an INT and return to caller.
    
        # PARAMETERS:
            *   candidate (Any): The object to validate.

        # Returns:
        BuildResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullXComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException
            
        # Notes
        See chess.system.config.LONGEST_KNIGHT_LEG_SIZE for more details.
        """
        method = "VectorValidator._validate_x_component"
        
        try:
            if candidate is None:
                return BuildResult.failure(
                    NullXComponentException(
                        f"{method}: "
                        f"{NullXComponentException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, int):
                return BuildResult.failure(
                    TypeError(f"{method}: "
                              f"Expected an int, got {type(candidate).__name__} instead.")
                )
            x = cast(int, candidate)
            
            if x < -LONGEST_KNIGHT_LEG_SIZE:
                return BuildResult.failure(
                    VectorBelowBoundsException(
                        f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if x >= LONGEST_KNIGHT_LEG_SIZE:
                return BuildResult.failure(
                    VectorAboveBoundsException(
                        f"{method}: "
                        f"{VectorAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(payload=x)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    ex=ex,
                    message=f"{method}: "
                            f"{VectorBuildFailedException.DEFAULT_MESSAGE}",
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_y_component(cls, candidate: Any) -> BuildResult[int]:
        """
        # ACTION:
        1.  Test if candidate is:
                *   not validation
                *   is an int
                *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE] exclusive.
        2.  If any check fails return its exception inside a BuildResult.
        3.  Otherwise, cast candidate to an INT and return to caller.

        # PARAMETERS:
            *   candidate (Any): The object to validate.

        # Returns:
        BuildResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullYComponentException
            *   VectorBelowBoundsException
            *   VectorAboveBoundsException
            *   InvalidVectorException

        # Notes
        See chess.system.config.LONGEST_KNIGHT_LEG_SIZE for more details.
        """
        method = "VectorValidator._validate_y_component"
        
        try:
            if candidate is None:
                return BuildResult.failure(
                    NullYComponentException(
                        f"{method}: "
                        f"{NullYComponentException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, int):
                return BuildResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected an int, got {type(candidate).__name__} instead."
                    )
                )
            y = cast(int, candidate)
            
            if y < -LONGEST_KNIGHT_LEG_SIZE:
                return BuildResult.failure(
                    VectorBelowBoundsException(
                        f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if y >= LONGEST_KNIGHT_LEG_SIZE:
                return BuildResult.failure(
                    VectorAboveBoundsException(
                        f"{method}: "
                        f"{VectorAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(payload=y)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    ex=ex,
                    message=f"{method}: "
                            f"{VectorBuildFailedException.DEFAULT_MESSAGE}",
                )
            )