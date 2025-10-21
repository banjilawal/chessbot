# src/chess/system/name/travel_exception.py

"""
Module: chess.system.name.exception
Author: Banji Lawal
Created: 2025-09-17
Updated: 2025-10-10
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `NameValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the exception being raised.
       `NameValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying names.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ValidationException`, `BlankStringException`, `NullException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `InvalidNameException`,`NullNameException`).
"""

from chess.system import NullException, ValidationException, BlankStringException


__all__ = [
  'InvalidNameException',
  'BlankNameException',
  'ShortNameException',
  'LongNameException',
  'NullNameException',
]


class InvalidNameException(ValidationException):
  """
  Super class of exceptions raised by `NameValidator`. Subclasses give details useful for debugging. Exists primarily
  to allow catching and wrapping all errors discovered validating names. DO NOT USE DIRECTLY.
  """
  ERROR_CODE = "NAME_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Name Validation failed"

class BlankNameException(InvalidNameException, BlankStringException):
  """
  Name with only white space raises BlankNameException
  """
  ERROR_CODE = "BLANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Name cannot be white space only"


class ShortNameException(InvalidNameException):
  """
  Name below the minimum length raises ShortNameException. See documentation or
  chess.system.config for MIN_NAME_LENGTH.
  """
  ERROR_CODE = "SHORT_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is below the minimum length"


class LongNameException(InvalidNameException):
  """
  Name is longer than MAX_NAME_LENGTH raises LongNameException.
  """
  ERROR_CODE = "LONG_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is above the maximum length"


class NullNameException(InvalidNameException, NullException):
  """
  Raised if an entity's name is null
  """
  ERROR_CODE = "NULL_NAME_ERROR"
  DEFAULT_MESSAGE = f"Name cannot be null"

