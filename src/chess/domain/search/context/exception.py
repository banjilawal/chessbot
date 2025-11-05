# src/chess/domain/search/context/exception.py

"""
Module: chess.domain.search.context.exception
Created: 2025-11-05
version: 1.0.0
"""


from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    'DomainSearchContextException',

    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullDomainSearchContextException',
    'InvalidDomainSearchContextException',
    'ZeroDomainSearchParamsException',
    'TooManyDomainSearchParamsException',
    'DomainRansomParamBoundsException',
    'DomainInvalidRankNameParamException',

    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'DomainSearchContextBuildFailedException',
]


class DomainSearchContextException(ContextException):
    """
    Super class for exceptions raised by DomainSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "DOMAIN_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "DomainSearchContext raised an rollback_exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullDomainSearchContextException(DomainSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team domainSearchContext but
    gets null instead.
    """
    ERROR_CODE = "NULL_SEARCH_DOMAIN_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "DomainSearchContext cannot be null"


class InvalidDomainSearchContextException(DomainSearchContextException, ValidationException):
    """
    Raised by domainSearchContextBValidator if domainSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing domainSearchContext
    """
    ERROR_CODE = "DOMAIN_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "DomainSearchContext validator failed."


class ZeroDomainSearchParamsException(DomainSearchContextException):
    """
    Raised if all DomainSearchContext params are set null.
    """
    ERROR_CODE = "ZERO_DOMAIN_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A DomainSearchContext cannot have no params selected. Pick one param to run a search."
    )

class TooManyDomainSearchParamsException(DomainSearchContextException):
    """
    Raised if more than one DomainSearchContext param is set null.
    """
    ERROR_CODE = "TOO_MANY_DOMAIN_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one DomainSearchContext param was set. If more than one param is set a search cannot be run."
    )

class DomainRansomParamBoundsException(DomainSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "DOMAIN_SEARCH_CONTEXT_RANSOM_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "The ransom is out of bounds. It cannot be used in DomainSearchContext."

class DomainInvalidRankNameParamException(DomainSearchContextException):
  """
  If the old_search context is out of bounds there might be other problems.
  Instead of running team old_search that won'candidate produce team notification, raise this
  error.
  """
  ERROR_CODE = "DOMAIN_SEARCH_CONTEXT_RANK_NAME_ERROR"
  DEFAULT_MESSAGE = "The rank name is not recognized. It cannot be used in DomainSearchContext."


# #======================#   PIECE_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class DomainSearchContextBuildFailedException(DomainSearchContextException, BuildFailedException):
    """
    Raised when DomainSearchContextBuilder encounters an error while building team team.
    Exists primarily to catch all exceptions raised build team new domainSearchContext
    """
    ERROR_CODE = "DOMAIN_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "DomainSearchContext build failed."
