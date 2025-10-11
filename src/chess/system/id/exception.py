# src/chess/system/id/exception.py

"""
Module: chess.system.id.exception
Author: Banji Lawal
Created: 2025-09-17
Updated: 2025-10-10
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
    `ValidationException`, `NullException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `InvalidIdException`,`IdNullException`).
"""


from chess.system import ValidationException, NullException


__all__ = [
  'InvalidIdException',
  'IdNullException',
  'NegativeIdException'
]

class InvalidIdException(ValidationException):
  """
  Super class of exceptions raised by `IdValidator`. Subclasses give details useful for
  debugging. Exists primarily to allow catching and wrapping all errors discovered validating ids.
  DO NOT USE DIRECTLY.
  """
  ERROR_CODE = "ID_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Id Validation failed."

class IdNullException(NullException):
  """
  Raised if an entity's id is null
  """
  ERROR_CODE = "NULL_ID_ERROR"
  DEFAULT_MESSAGE = "Id cannot be null."


class NegativeIdException(InvalidIdException):
  """Raised if an id is zero or less"""
  ERROR_CODE = "ID_IS_NEGATIVE"
  DEFAULT_MESSAGE = "Id cannot be negative."


