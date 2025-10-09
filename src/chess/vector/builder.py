# src/chess/vector/builder.py
"""
Module: chess.vector.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
**Limitation**: There is no guarantee properly created `Vector` objects released by the
    module will satisfy client requirements. Clients are responsible for ensuring a `VectorBuilder`
    product will not fail when used. Products from `VectorBuilder` --should-- satisfy
    `VectorValidator` requirements.

**Related Features**:
    Authenticating existing vectors -> See VectorValidator, module[chess.vector.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

# PURPOSE:
---------
1. Central, single producer of authenticated `Vector` objects.
2. Putting all the steps and logging into one place makes modules using `Vector` objects
    cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
  * `BuildResult`, `Builder`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.vector`:
    `Vector`, `VectorBuildFailedException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`,`VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
----------
 * `VectorBuilder`
"""

# src/chess/vector/validation.py
"""
Module: chess.vector.validator
Author: Banji Lawal
Created: 2025-10-08

# SCOPE:
**Limitation**: This module cannot prevent classes, processes or modules using `Vector`
    instances that pass sanity checks will not fail when using the validated `Vector`.
    Once client's processes might fail, experience data inconsistency or have other 
    faults.

**Related Features**:
    Building vectors -> See VectorBuilder, module[chess.vector.builder], 
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]





# DEPENDENCIES:
From `chess.system`:
  * `ValidationResult`, `Validator`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.vector`:
    `Vector`, `NullVectorException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
 * `VectorValidator`
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
