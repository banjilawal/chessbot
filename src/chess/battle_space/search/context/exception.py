"""
Module: chess.projectionSearchContext.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of **TeamSearchContext objects**. It handles boundary checks (row/column)
limits and validation checks. It does not contain any logic for *raising* these exception; that responsibility
falls to the `BoardSearchContextValidator` and `ProjectionSearchContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team_name
highly granular and hierarchical set of exception, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `ProjectionSearchContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `TeamSearchContext` graph.
It abstracts underlying Python exception into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exception: `ChessException`, `ValidationFailedException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exception in the `__all__` list following (e.g., `ProjectionSearchContextException`,
`NullProjectionSearchContextException`, `RowAboveBoundsException`).
"""

from chess.rank import RankSpec
from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'ProjectionSearchContextException',

    #======= SEARCH_CONTEXT VALIDATION EXCEPTION =======#
    'NullProjectionSearchContextException',
    'InvalidProjectionSearchContextException',
    # 'ProjectionSearchContextZeroParamCountException',
    # 'ProjectionSearchContextMaxParamCountException',

    #======= SEARCH_CONTEXT BUILD EXCEPTION =======#
    'ProjectionSearchContextBuildFailedException',
    'RansomOutOfBoundsException'
]


class ProjectionSearchContextException(ContextException):
    """
    Super class for exception raised by TeamSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext raised an exception."


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTION #======================# 
class NullProjectionSearchContextException(ProjectionSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name projectionSearchContext but
    gets validation instead.
    """
    ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext cannot be validation"


class InvalidProjectionSearchContextException(ProjectionSearchContextException, ValidationException):
    """
    Raised by projectionSearchContextBValidator if projectionSearchContext fails sanity checks. Exists primarily to
    catch all exception raised validating an existing projectionSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext validation failed."


class ProjectionSearchContextZeroParamCountException(ProjectionSearchContextException):
    """
    Raised if all TeamSearchContext params are set validation.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ZERO_PARAM_ERROR"
    DEFAULT_MESSAGE = "A TeamSearchContext cannot have all params set validation."


class ProjectionSearchContextMaxParamCountException(ProjectionSearchContextException):
    """
    Raised if more than one TeamSearchContext param is set validation.
    """
    ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "A TeamSearchContext cannot have more than one param set validation."


# #======================#   PROJECTION_SEARCH_CONTEXT BUILD EXCEPTION #======================# 
class ProjectionSearchContextBuildFailedException(ProjectionSearchContextException, BuildFailedException):
    """
    Raised when ProjectionSearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exception raised builder team_name new projectionSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext build failed."

class RansomOutOfBoundsException(ProjectionSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team_name old_search that won'candidate produce team_name notification, raise this
  error.
  """
  ERROR_CODE = "RANSOM_IN_SEARCH_CONTEXT_OUT_BOUNDS_ERROR"
  DEFAULT_MESSAGE = (
      f"The `TeamSearchContext.ransom` is out of bounds. Ransoms are "
      f"between {RankSpec.KING.ransom} and {RankSpec.QUEEN.ransom} inclusive."
  )
#=========================================================================#
#======================= FILTER_CONTEXT EXCEPTION =======================#
#=========================================================================#
