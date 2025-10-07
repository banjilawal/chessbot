# src/chess.coord.exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide a
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.system import PieceSearchContextException


class TeamPieceSearchContextException(PieceSearchContextException):
    ERROR_CODE = "TEAM_SEARCH_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "TeamPieceSearchContext raised an exception."


# src/chess.pieceSearchContext.exception.py

"""
Module: chess.pieceSearchContext.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **PieceSearchContext objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `PieceSearchContextValidator` and `PieceSearchContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide a
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `PieceSearchContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `PieceSearchContext` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `PieceSearchContextException`,
`NullPieceSearchContextException`, `RowAboveBoundsException`).
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
    'PieceSearchContextException',
    'PieceFilterContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullPieceSearchContextException',
    'InvalidPieceSearchContextException',
    'PieceSearchContextZeroParamCountException',
    'PieceSearchContextMaxParamCountException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'PieceSearchContextBuildFailedException',

    # ======= FILTER_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullPieceFilterContextException',
    'InvalidPieceFilterContextException',
    'PieceFilterContextZeroParamCountException',
    'PieceFilterContextMaxParamCountException',

    # ======= FILTER_CONTEXT BUILD EXCEPTIONS =======#
    'PieceFilterContextBuildFailedException',
]


class PieceSearchContextException(ContextException):
    """
    Super class for exceptions raised by PieceSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceSearchContext raised an team_exception"


# ======================#  SEARCH_CONTEXT VALIDATION EXCEPTIONS ======================#
class NullPieceSearchContextException(PieceSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires a pieceSearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceSearchContext cannot be null"


class InvalidPieceSearchContextException(PieceSearchContextException, ValidationException):
    """
    Raised by pieceSearchContextBValidator if pieceSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing pieceSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceSearchContext validation failed."


class PieceSearchContextZeroParamCountException(PieceSearchContextException):
    """
    Raised if all PieceSearchContext params are set null.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ZERO_PARAM_ERROR"
    DEFAULT_MESSAGE = "A PieceSearchContext cannot have all params set null."


class PieceSearchContextMaxParamCountException(PieceSearchContextException):
    """
    Raised if more than one PieceSearchContext param is set null.
    """
    ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "A PieceSearchContext cannot have more than one param set null."


# ======================#  SEARCH_CONTEXT BUILD EXCEPTIONS ======================#
class PieceSearchContextBuildFailedException(PieceSearchContextException, BuildFailedException):
    """
    Raised when PieceSearchContextBuilder encounters an error while building a team.
    Exists primarily to catch all exceptions raised build a new pieceSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "PieceSearchContext build failed."


# =========================================================================#
# ======================= FILTER_CONTEXT EXCEPTIONS =======================#
# =========================================================================#

class PieceFilterContextException(PieceSearchContextException):
    """
    Super class for exceptions raised by PieceFilterContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "FILTER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceFilterContext raised an team_exception"


# ======================#  FILTER_CONTEXT VALIDATION EXCEPTIONS ======================#
class NullPieceFilterContextException(PieceFilterContextException, NullException):
    """
    Raised if an entity, method, or operation requires a pieceFilterContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_FILTER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceFilterContext cannot be null"


class InvalidPieceFilterContextException(PieceFilterContextException, ValidationException):
    """
    Raised by pieceFilterContextBValidator if pieceFilterContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing pieceFilterContext
    """
    ERROR_CODE = "FILTER_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PieceFilterContext validation failed."


class PieceFilterContextZeroParamCountException(PieceFilterContextException):
    """
    Raised if all PieceFilterContext params are set null.
    """
    ERROR_CODE = "FILTER_CONTEXT_ZERO_PARAM_ERROR"
    DEFAULT_MESSAGE = "A PieceFilterContext cannot have all params set null."


class PieceFilterContextMaxParamCountException(PieceFilterContextException):
    """
    Raised if more than one PieceFilterContext param is set null.
    """
    ERROR_CODE = "FILTER_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "A PieceFilterContext cannot have more than one param set null."


# ======================#  FILTER_CONTEXT BUILD EXCEPTIONS ======================#
class PieceFilterContextBuildFailedException(PieceFilterContextException, BuildFailedException):
    """
    Raised when PieceFilterContextBuilder encounters an error while building a team.
    Exists primarily to catch all exceptions raised build a new pieceFilterContext
    """
    ERROR_CODE = "FILTER_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "PieceFilterContext build failed."

