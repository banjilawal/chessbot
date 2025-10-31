# src/chess/system/notification/rollback_exception.py

"""
Module: chess.system.notification.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's effects and actions cover exceptions raised by `Result` instances.

# SECTION 3: Limitations
  1. Does not provide granular, precise information pertinent to debugging. The module's
      scope it too wide for that.
  2. `ResultException` classes only cover their constructor.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Ensuring validator results are communicated are sent to clients is an integrity feature.

# SECTION 6 - Feature Delivery Mechanism:
  1. Verify existing entities meet minimum requirements for use in the system.
  2. A description of an error condition, boundary violation, experienced or caused by an entity in
      the validator graph.
  3. The root of a scalable, modular hierarchy for validator related exceptions.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `ResultException`).
"""


from chess.system import ChessException

__all__ = [
  'ResultException',

#====================== RESULT CONSTRUCTOR EXCEPTIONS #======================#  
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
  DEFAULT_MESSAGE = "Result raised an rollback_exception."


class ResultConstructorException(ResultException):
  """
  Base class for exceptions about `Result` constructors. A `Result` must
  have one-and-only-one parameter that is not null. This is the super class
  for cases:
    No params
    Both params
  """
  ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "Invalid constructor params raised an rollback_exception."


class EmptyResultConstructorException(ResultConstructorException):
  """
  Raised if team `Result` object's constructor is empty.
  """
  ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
  """
  Raised if both payload and error params are not null
  when constructing team `Result` object.
  """
  ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
  DEFAULT_MESSAGE = (
    "A Result cannot have both its payload and error set. Construct "
    "with either payload or rollback_exception, no both."
  )




