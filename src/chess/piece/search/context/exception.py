"""
Module: chess.discoverySearchContext.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **DiscoverySearchContext objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `DiscoverySearchContextValidator` and `DiscoverySearchContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `DiscoverySearchContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `DiscoverySearchContext` domain.
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
See the list of exceptions in the `__all__` list following (e.g., `DiscoverySearchContextException`,
`NullDiscoverySearchContextException`, `RowAboveBoundsException`).
"""

from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'DiscoverySearchContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullDiscoverySearchContextException',
    'InvalidDiscoverySearchContextException',
    'ZeroDiscoverySearchParamsException',
    'TooManyDiscoverySearchParamsException',
    'DiscoveryRansomParamBoundsException',
    'DiscoveryInvalidRankNameParamException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'DiscoverySearchContextBuildFailedException',
]


class DiscoverySearchContextException(ContextException):
    """
    Super class for exceptions raised by DiscoverySearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "DISCOVERY_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "DiscoverySearchContext raised an exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullDiscoverySearchContextException(DiscoverySearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team discoverySearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_DISCOVERY_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "DiscoverySearchContext cannot be null"


class InvalidDiscoverySearchContextException(DiscoverySearchContextException, ValidationException):
    """
    Raised by discoverySearchContextBValidator if discoverySearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing discoverySearchContext
    """
    ERROR_CODE = "DISCOVERY_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "DiscoverySearchContext validation failed."


class ZeroDiscoverySearchParamsException(DiscoverySearchContextException):
    """
    Raised if all DiscoverySearchContext params are set null.
    """
    ERROR_CODE = "ZERO_DISCOVERY_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A DiscoverySearchContext cannot have no params selected. Pick one param to run a search."
    )

class TooManyDiscoverySearchParamsException(DiscoverySearchContextException):
    """
    Raised if more than one DiscoverySearchContext param is set null.
    """
    ERROR_CODE = "TOO_MANY_DISCOVERY_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one DiscoverySearchContext param was set. If more than one param is set a search cannot be run."
    )

class DiscoveryRansomParamBoundsException(DiscoverySearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "DISCOVERY_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The ransom is out of bounds. It cannot be used in DiscoverySearchContext."

class DiscoveryInvalidRankNameParamException(DiscoverySearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "DISCOVERY_SEARCH_CONTEXT_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "The rank name is not recognized. It cannot be used in DiscoverySearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class DiscoverySearchContextBuildFailedException(DiscoverySearchContextException, BuildFailedException):
    """
    Raised when DiscoverySearchContextBuilder encounters an error while building team team.
    Exists primarily to catch all exceptions raised build team new discoverySearchContext
    """
    ERROR_CODE = "DISCOVERY_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "DiscoverySearchContext build failed."


# =========================================================================#
# ======================= FILTER_CONTEXT EXCEPTIONS =======================#
# =========================================================================#
