# src/chess/graph/search/context/exception.py

"""
Module: chess.graph.search.context.exception
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'GraphSearchContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullGraphSearchContextException',
    'InvalidGraphSearchContextException',
    'ZeroGraphSearchParamsException',
    'TooManyGraphSearchParamsException',
    'GraphRansomParamBoundsException',
    'GraphInvalidRankNameParamException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'GraphSearchContextBuildFailedException',
]


class GraphSearchContextException(ContextException):
    """
    Super class for exceptions raised by GraphSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "GRAPH_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "GraphSearchContext raised an rollback_exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullGraphSearchContextException(GraphSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team graphSearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_GRAPH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "GraphSearchContext cannot be null"


class InvalidGraphSearchContextException(GraphSearchContextException, ValidationException):
    """
    Raised by graphSearchContextBValidator if graphSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing graphSearchContext
    """
    ERROR_CODE = "GRAPH_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GraphSearchContext validator failed."


class ZeroGraphSearchParamsException(GraphSearchContextException):
    """
    Raised if all GraphSearchContext params are set null.
    """
    ERROR_CODE = "ZERO_GRAPH_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A GraphSearchContext cannot have no params selected. Pick one param to run a search."
    )

class TooManyGraphSearchParamsException(GraphSearchContextException):
    """
    Raised if more than one GraphSearchContext param is set null.
    """
    ERROR_CODE = "TOO_MANY_GRAPH_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one GraphSearchContext param was set. If more than one param is set a search cannot be run."
    )

class GraphRansomParamBoundsException(GraphSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "GRAPH_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The ransom is out of bounds. It cannot be used in GraphSearchContext."

class GraphInvalidRankNameParamException(GraphSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "GRAPH_SEARCH_CONTEXT_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "The bounds name is not recognized. It cannot be used in GraphSearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class GraphSearchContextBuildFailedException(GraphSearchContextException, BuildFailedException):
    """
    Raised when GraphSearchContextBuilder encounters an error while building team team.
    Exists primarily to catch all exceptions raised build team new graphSearchContext
    """
    ERROR_CODE = "GRAPH_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "GraphSearchContext build failed."
