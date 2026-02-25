# src/chess/neighbor/searcher/collision.py

"""
Module: chess.neighbor.searcher.exception
Created: 2025-11-05
version: 1.0.0
"""


from chess.system import ContextException, NullException, BuildException, ValidationException

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
    'VisitationSearchContextBuildException',
]


class VisitationSearchContextException(ContextException):
    """
    Super class for exception raised by VisitationSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging msgs.
    """
    ERR_CODE = "VISITATION_SEARCH_CONTEXT_ERROR"
    MSG = "VisitationSearchContext raised an exception."


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTION #======================#
class NullVisitationSearchContextException(VisitationSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name visitationSearchContext but
    gets validation instead.
    """
    ERR_CODE = "NULL_SEARCH_VISITATION_CONTEXT_ERROR"
    MSG = "VisitationSearchContext cannot be validation"


class InvalidVisitationSearchContextException(VisitationSearchContextException, ValidationException):
    """
    Raised by visitationSearchContextBValidator if visitationSearchContext fails sanity checks. Exists primarily to
    catch all exception raised validating an existing visitationSearchContext
    """
    ERR_CODE = "VISITATION_SEARCH_CONTEXT_VALIDATION_ERROR"
    MSG = "VisitationSearchContext validation failed."


class ZeroVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if all VisitationSearchContext params are set validation.
    """
    ERR_CODE = "ZERO_VISITATION_SEARCH_PARAMS_ERROR"
    MSG = (
        "A VisitationSearchContext cannot have no params selected. Pick one param to run a searcher."
    )

class ExcessiveVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if more than one VisitationSearchContext param is set validation.
    """
    ERR_CODE = "TOO_MANY_VISITATION_SEARCH_PARAMS_ERROR"
    MSG = (
        "More than one VisitationSearchContext param was set. If more than one param is set a searcher cannot be run."
    )

class VisitationRansomParamBoundsException(VisitationSearchContextException):
  """
  If the old_search map is out of bounds there might be other problems.
  Instead of running team_name old_search that won'candidate produce team_name notification, raise this
  error.
  """
  ERR_CODE = "VISITATION_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  MSG = "The visitor_ransom is out of bounds. It cannot be used in VisitationSearchContext."

class VisitationInvalidRankNameParamException(VisitationSearchContextException):
  """
  If the old_search map is out of bounds there might be other problems.
  Instead of running team_name old_search that won'candidate produce team_name notification, raise this
  error.
  """
  ERR_CODE = "VISITATION_SEARCH_CONTEXT_RANK_NAME_ERROR"
  MSG = "The bounds visitor_name is not recognized. It cannot be used in VisitationSearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTION #======================#
class VisitationSearchContextBuildException(VisitationSearchContextException, BuildException):
    """
    Raised when VisitationSearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exception raised builder team_name new visitationSearchContext
    """
    ERR_CODE = "VISITATION_SEARCH_CONTEXT_BUILD_FAILED"
    MSG = "VisitationSearchContext build failed."
