# src/chess/neighbor/searcher/collision.py

"""
Module: chess.neighbor.searcher.exception
Created: 2025-11-05
version: 1.0.0
"""


from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'VisitationSearchContextException',

    #======= SEARCH_CONTEXT VALIDATION EXCEPTION =======#
    'NullVisitationSearchContextException',
    'InvalidVisitationSearchContextException',
    'ZeroVisitationSearchParamsException',
    'ExcessiveVisitationSearchParamsException',
    'VisitationRansomParamBoundsException',
    'VisitationInvalidRankNameParamException',

    #======= SEARCH_CONTEXT BUILD EXCEPTION =======#
    'VisitationSearchContextBuildFailedException',
]


class VisitationSearchContextException(ContextException):
    """
    Super class for exception raised by VisitationSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext raised an exception."


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTION #======================#
class NullVisitationSearchContextException(VisitationSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name visitationSearchContext but
    gets validation instead.
    """
    ERROR_CODE = "NULL_SEARCH_VISITATION_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext cannot be validation"


class InvalidVisitationSearchContextException(VisitationSearchContextException, ValidationException):
    """
    Raised by visitationSearchContextBValidator if visitationSearchContext fails sanity checks. Exists primarily to
    catch all exception raised validating an existing visitationSearchContext
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext validation failed."


class ZeroVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if all VisitationSearchContext params are set validation.
    """
    ERROR_CODE = "ZERO_VISITATION_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A VisitationSearchContext cannot have no params selected. Pick one param to run a searcher."
    )

class ExcessiveVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if more than one VisitationSearchContext param is set validation.
    """
    ERROR_CODE = "TOO_MANY_VISITATION_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one VisitationSearchContext param was set. If more than one param is set a searcher cannot be run."
    )

class VisitationRansomParamBoundsException(VisitationSearchContextException):
  """
  If the old_search map is out of bounds there might be other problems.
  Instead of running team_name old_search that won'candidate produce team_name notification, raise this
  error.
  """
  ERROR_CODE = "VISITATION_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The visitor_ransom is out of bounds. It cannot be used in VisitationSearchContext."

class VisitationInvalidRankNameParamException(VisitationSearchContextException):
  """
  If the old_search map is out of bounds there might be other problems.
  Instead of running team_name old_search that won'candidate produce team_name notification, raise this
  error.
  """
  ERROR_CODE = "VISITATION_SEARCH_CONTEXT_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "The bounds visitor_name is not recognized. It cannot be used in VisitationSearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTION #======================#
class VisitationSearchContextBuildFailedException(VisitationSearchContextException, BuildFailedException):
    """
    Raised when VisitationSearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exception raised builder team_name new visitationSearchContext
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "VisitationSearchContext build failed."
