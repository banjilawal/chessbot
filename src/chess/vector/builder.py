# chess/vector/builder.py

"""
Module: chess.vector.builder
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from typing import Any, cast

from chess.system import Builder, BuildResult, LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, VectorBuildFailedException, NullXComponentException, NullYComponentException,
    VectorBelowBoundsException, VectorAboveBoundsException
)


class VectorBuilder(Builder[Vector]):
    """
    # ROLE: Builder, Guarantee Data Integrity

    # RESPONSIBILITIES:
    Produce Coord instances whose integrity is always guaranteed. If any attributes do not pass their integrity checks,
    send an exception instead.

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
        1.  Check x is:
            *   an INT
            *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE inclusive.
        2.  Check y is:
            *   an INT
            *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE inclusive.
        3.  If any check fails, return the exception inside a BuildResult.
        2.  When all checks create a new Vector and return in a BuildResult

        PARAMETERS:
            *   x (int): value in the x-plane
            *   y (int): value in the y-plane

        # Returns:
        BuildResult[Vector] containing either:
            - On success: T in payload.
            - On failure: Exception.

        RAISES:
            *   VectorBuildFailedException
        """
        method = "VectorBuilder.build"
        
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
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_x_component(cls, candidate: Any) -> BuildResult[int]:
        """
        # ACTION:
        1.  Test if candidate is:
                *   not null
                *   is an int
                *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE] exclusive.
        2.  If any check fails return its exception inside a BuildResult.
        3.  Otherwise cast candidate to an INT and return to caller.
    
        # PARAMETERS:
            *   candidate (Any): The object to validate.

        # Returns:
        BuildResult[int] containing either:
            - On success: int in payload.
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
                        f"{method}: {NullXComponentException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, int):
                return BuildResult.failure(
                    TypeError(f"{method}: Expected an int, got {type(candidate).__name__} instead.")
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
                        f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(payload=x)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_y_component(cls, candidate: Any) -> BuildResult[int]:
        """
        # ACTION:
        1.  Test if candidate is:
                *   not null
                *   is an int
                *   between -LONGEST_KNIGHT_LEG_SIZE and LONGEST_KNIGHT_LEG_SIZE] exclusive.
        2.  If any check fails return its exception inside a BuildResult.
        3.  Otherwise, cast candidate to an INT and return to caller.

        # PARAMETERS:
            *   candidate (Any): The object to validate.

        # Returns:
        BuildResult[int] containing either:
            - On success: int in payload.
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
                        f"{method}: {NullYComponentException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, int):
                return BuildResult.failure(
                    TypeError(
                        f"{method}: Expected an int, got {type(candidate).__name__} instead."
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
                        f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(payload=y)
        
        except Exception as ex:
            return BuildResult.failure(
                VectorBuildFailedException(
                    f"{method}: {VectorBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )