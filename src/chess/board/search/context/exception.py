"""
Module: chess.pieceSearchContext.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validation, and manipulation of **BoardSearchContext objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `BoardSearchContextValidator` and `PieceSearchContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `PieceSearchContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `BoardSearchContext` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `PieceSearchContextException`,
`NullPieceSearchContextException`, `RowAboveBoundsException`).
"""

from chess.rank import RankSpec
from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'PieceSearchContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullPieceSearchContextException',
    'InvalidPieceSearchContextException',
    # 'PieceSearchContextZeroParamCountException',
    # 'PieceSearchContextMaxParamCountException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'PieceSearchContextBuildFailedException',
    'RansomOutOfBoundsException'
]


class PieceSearchContextException(ContextException):
    """
    Super class for exceptions raised by BoardSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "BoardSearchContext raised an rollback_exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullPieceSearchContextException(PieceSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team pieceSearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "BoardSearchContext cannot be null"


class InvalidPieceSearchContextException(PieceSearchContextException, ValidationException):
    """
    Raised by pieceSearchContextBValidator if pieceSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing pieceSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "BoardSearchContext validation failed."


class PieceSearchContextZeroParamCountException(PieceSearchContextException):
    """
    Raised if all BoardSearchContext params are set null.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ZERO_PARAM_ERROR"
    DEFAULT_MESSAGE = "A BoardSearchContext cannot have all params set null."


class PieceSearchContextMaxParamCountException(PieceSearchContextException):
    """
    Raised if more than one BoardSearchContext param is set null.
    """
    ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "A BoardSearchContext cannot have more than one param set null."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class PieceSearchContextBuildFailedException(PieceSearchContextException, BuildFailedException):
    """
    Raised when PieceSearchContextBuilder encounters an error while building team team.
    Exists primarily to catch all exceptions raised build team new pieceSearchContext
    """
    ERROR_CODE = "SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "BoardSearchContext build failed."

class RansomOutOfBoundsException(PieceSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "RANSOM_IN_SEARCH_CONTEXT_OUT_BOUNDS_ERROR"
  DEFAULT_MESSAGE = (
      f"The `BoardSearchContext.ransom` is out of bounds. Ransoms are "
      f"between {RankSpec.KING.ransom} and {RankSpec.QUEEN.ransom} inclusive."
  )
# =========================================================================#
# ======================= FILTER_CONTEXT EXCEPTIONS =======================#
# =========================================================================#
