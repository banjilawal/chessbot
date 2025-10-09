# src/chess/vector/builder.py
"""
Module: chess.vector.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Building, Single responsibilities,
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:
From `chess.system`:
  * `BuildResult`, `Builder`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.vector`:
    `Vector`, `VectorBuildFailedException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`,`VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
 * `VectorBuilder`
"""

from chess.system import Builder, BuildResult, KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, InvalidVectorException, NullXComponentException, NullYComponentException,
    VectorBelowBoundsException, VectorAboveBoundsException
)

class VectorBuilder(Builder[Vector]):
    """
    # ROLE: Builder

    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `Vector` instances.
    2. Create new `Vector` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.

    # PROVIDES:
    `BuildResult`: Return type containing the built `Vector` or error information.

    # ATTRIBUTES:
    None
    """

    @classmethod
    def build(cls, x: int, y: int) -> BuildResult[Vector]:
        """
        ACTION:
        Create a `Vector` object if the parameters have correctness.

        PARAMETERS:
            * `x` (`int`): value in the x-plane
            * `y` (`int`): value in the y-plane

        RETURNS:
        `BuildResult[Vector]`: A `BuildResult` containing either:
            `'payload'` - A valid `Vector` instance in the payload
            `exception` - Error information and error details

        RAISES:
        `VectorBuildFailedException`: Wraps any specification violations including:
            * `NullXComponentException`: if `x` is None
            * `NullYComponentException`: if `y` is None
            * `VectorBelowBoundsException`: if `x` or `y` < -KNIGHT_STEP_SIZE
            * `VectorAboveBoundsException`: if `x` or `y` > KNIGHT_STEP_SIZE
        """
        method = "VectorBuilder.build"

        try:
            # Handle the x-component
            if x is None:
                ex = NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            if x < -KNIGHT_STEP_SIZE:
                ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            if x > KNIGHT_STEP_SIZE:
                ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            # Handle the y-component
            if y is None:
                ex = NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            if y < -KNIGHT_STEP_SIZE:
                ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            if y > KNIGHT_STEP_SIZE:
                ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=ex)

            return BuildResult(payload=Vector(x=x, y=y))

        except (
            NullXComponentException,
            NullYComponentException,
            VectorBelowBoundsException,
            VectorAboveBoundsException
        ) as e:
            raise VectorBuildFailedException(f"{method}: {e}")

        # This block catches any unexpected exceptions, logs and re
        except Exception as e:
            LoggingLevelRouter.route_error(context=VectorBuilder, exception=e)
            raise VectorBuildFailedException(f"{method}: {e}")
