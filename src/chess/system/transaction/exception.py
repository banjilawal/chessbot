# src/chess/system/event/travel_exception.py

"""
Module: chess.system.event.exception
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

from chess.system import ChessException, ResultException, ContextException


__all__ = [
  'TransactionException',
  'TransactionResultException',
]


class TransactionException(ChessException):
  """
  Super class of all exceptions `Transaction` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Transaction`
  exceptions.
  """
  ERROR_CODE = "TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction raised an exception."


#======================# EVENT VALIDATION EXCEPTIONS #======================#


class TransactionResultException(ResultException):
  """
  Super class of all exceptions `TransactionResult` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `TransactionResult`
  exceptions.
  """
  ERROR_CODE = "TRANSACTION_RESULT_ERROR"
  DEFAULT_MESSAGE = "TransactionResult raised an exception."


