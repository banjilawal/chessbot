# /src/chess/system/result/exception.py

"""
Module: `chess.system.result.exception`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
Responsibilities: Holds exceptions organic to `Result` objects

Contains:
See the list of exception in the `__alL__` list following
"""

"""
Result exceptions are about `Result` construction not the contents of the result. A `ResultException` is
raised by `Builder` objects.
"""

from chess.system import ChessException

__all__ = [
    'ResultException',

    # === RESULT CONSTRUCTOR EXCEPTIONS ===
    'ResultConstructorException',
    'EmptyResultConstructorException',
    'ErrorContradictsPayloadException'
]

class ResultException(ChessException):
    """
    Super class of exceptions organic to `Result` objects. DO NOT USE DIRECTLY. Subclasses give
    details useful for debugging. `ResultException` exists primarily to allow catching all `Result`
    exceptions.
    """
    ERROR_CODE = "RESULT_ERROR"
    DEFAULT_MESSAGE = "Result raised an exception."


class ResultConstructorException(ResultException):
    """
    Base class for exceptions about `Result` constructors. A `Result` must
    have one-and-only-one parameter that is not null. This is the super class
    for cases:
        No params
        Both params
    """
    ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = "Invalid constructor params raised an exception."


class EmptyResultConstructorException(ResultConstructorException):
    """
    Raised if a `Result` object's constructor is empty.
    """
    ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
    DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
    """
    Raised if both payload and error params are not null
    when constructing a `Result` object.
    """
    ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
    DEFAULT_MESSAGE = (
        "A Result cannot have both its payload and error set. Construct "
        "with either payload or exception, no both."
    )







