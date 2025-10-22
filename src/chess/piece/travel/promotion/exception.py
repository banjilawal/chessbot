# src/chess/system/travel/travel_exception.py

"""
Module: chess.system.travel.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the exception being raised.
       `IdValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying ids.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""

# src/chess/vector/travel_exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.event import EventException, TransactionException
from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'PromotionEventException',

#====================== PROMOTION_EVENT VALIDATION EXCEPTIONS #======================#  
  'NullPromotionEventException',
  'InvalidPromotionEventException',

#====================== PROMOTION_EVENT BUILD EXCEPTIONS #======================#  
  'PromotionEventBuildFailed',

#====================== PROMOTION_TRANSACTION EXCEPTIONS #======================#  
  'PromotionTransactionException',
  'NullPromotionTransactionException',
]

class PromotionEventException(ChessException):
  """
  Super class of exceptions organic to `PromotionEven` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `PromotionEventException` exists primarily to allow catching all `PromotionEven`
  exceptions.
  """
  ERROR_CODE = "PROMOTION_EVENT_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent raised an exception."


#======================# PROMOTION_EVENT VALIDATION EXCEPTIONS #======================#  
class NullPromotionEventException(PromotionEventException, NullException):
  """Raised if an entity, method, or operation requires team `PromotionEvent` but gets null instead."""
  pass

class InvalidPromotionEventException(PromotionEventException, ValidationException):
  """
  Raised by PromotionEventValidator if team client fails sanity checks. Exists to catch all
  exceptions raised validating an existing `PromotionEvent` candidate.
  """
  ERROR_CODE = "PROMOTION_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent validation failed."


#======================# PROMOTION_EVENT BUILD EXCEPTIONS #======================#  
class PromotionEventBuildFailed(PromotionEventException, BuildFailedException):
  """
  Raised when `PromotionEventBuilder` crashed while building team new `PromotionEven`. Exists
  primarily to catch all exceptions raised creating `PromotionEvent` objects.
  """
  ERROR_CODE = "PROMOTION_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "PromotionEvent build failed."


#======================# PROMOTION_TRANSACTION EXCEPTIONS #======================#  
class PromotionTransactionException(TransactionException):
  """
  Wraps any errors raised during the promotion's lifecycle.
  """
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an exception."

class NullPromotionTransactionException(TransactionException):
  """Raised if an entity, method, or operation requires team `PromotionEvent` but gets null instead."""
  ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "PromotionTransaction raised an exception."
