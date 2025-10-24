# src/chess/vector/old_occupation_validator.py
"""
Module: chess.vector.validation
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation***: There is no guarantee properly created `Vector` objects released by the module will satisfy
    client requirements. Clients are responsible for ensuring a `VectorBuilder` product will not fail when used.

***Related Features***:
    Authenticating existing vectors -> See VectorValidator, module[chess.vector.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

***Design Concepts***:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Vector` objects.
2. Putting all the steps and logging into one place makes modules using `Vector` objects cleaner, easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`, `ChessException`, `NullException`
    `BuildFailedException`

From `chess.vector`:
    `Vector`, `NullVectorException`, `VectorBuildFailedException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
----------
 * `VectorBuilder`
"""

from chess.system import Builder, BuildResult, KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
    Vector, VectorBuildFailedException, NullXComponentException, NullYComponentException,
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
    @LoggingLevelRouter.monitor()
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
            `rollback_exception` - Error information and error details

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
                # ex =
                # LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, rollback_exception=ex)
                return BuildResult(exception=NullXComponentException(
                    f"{method}: {NullXComponentException.DEFAULT_MESSAGE}"
                ))

            if x < -KNIGHT_STEP_SIZE:
                # ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, rollback_exception=ex)
                return BuildResult(exception=VectorBelowBoundsException(
                    f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                ))

            if x > KNIGHT_STEP_SIZE:
                # ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, rollback_exception=ex)
                return BuildResult(exception=VectorAboveBoundsException(
                    f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                ))

            # Handle the y-component
            if y is None:
                # ex = NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, rollback_exception=ex)
                return BuildResult(exception=NullYComponentException(
                    f"{method}: {NullYComponentException.DEFAULT_MESSAGE}"
                ))

            if y < -KNIGHT_STEP_SIZE:
                # ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, rollback_exception=ex)
                return BuildResult(exception=VectorBelowBoundsException(
                    f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                ))

            if y > KNIGHT_STEP_SIZE:
                ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.log_and_raise_error(context=VectorBuilder, exception=ex)
                return BuildResult(exception=VectorAboveBoundsException(
                    f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                ))

            return BuildResult(payload=Vector(x=x, y=y))

        # This block lets the monitor log and re-raise the error.
        except Exception as e:
            return BuildResult(exception=VectorBuildFailedException(f"{method}: {e}"))
