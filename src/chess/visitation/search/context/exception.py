# src/chess/visitation/search/context/exception.py

"""
Module: chess.visitation.search.context.exception
Created: 2025-11-05
version: 1.0.0
"""


from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'VisitationSearchContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullVisitationSearchContextException',
    'InvalidVisitationSearchContextException',
    'ZeroVisitationSearchParamsException',
    'TooManyVisitationSearchParamsException',
    'VisitationRansomParamBoundsException',
    'VisitationInvalidRankNameParamException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'VisitationSearchContextBuildFailedException',
]


class VisitationSearchContextException(ContextException):
    """
    Super class for exceptions raised by VisitationSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext raised an rollback_exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullVisitationSearchContextException(VisitationSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team visitationSearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_VISITATION_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext cannot be null"


class InvalidVisitationSearchContextException(VisitationSearchContextException, ValidationException):
    """
    Raised by visitationSearchContextBValidator if visitationSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing visitationSearchContext
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext validator failed."


class ZeroVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if all VisitationSearchContext params are set null.
    """
    ERROR_CODE = "ZERO_VISITATION_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A VisitationSearchContext cannot have no params selected. Pick one param to run a search."
    )

class TooManyVisitationSearchParamsException(VisitationSearchContextException):
    """
    Raised if more than one VisitationSearchContext param is set null.
    """
    ERROR_CODE = "TOO_MANY_VISITATION_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one VisitationSearchContext param was set. If more than one param is set a search cannot be run."
    )

class VisitationRansomParamBoundsException(VisitationSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "VISITATION_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The ransom is out of bounds. It cannot be used in VisitationSearchContext."

class VisitationInvalidRankNameParamException(VisitationSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "VISITATION_SEARCH_CONTEXT_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "The rank name is not recognized. It cannot be used in VisitationSearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class VisitationSearchContextBuildFailedException(VisitationSearchContextException, BuildFailedException):
    """
    Raised when VisitationSearchContextBuilder encounters an error while building team team.
    Exists primarily to catch all exceptions raised build team new visitationSearchContext
    """
    ERROR_CODE = "VISITATION_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "VisitationSearchContext build failed."
