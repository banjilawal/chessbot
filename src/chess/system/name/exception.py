# src/chess/system/name/exception.py

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
The module's effects and actions cover exceptions raised by implementors of the `Validator` interface.

# SECTION 3: Limitations
  1. Does not provide granular, precise information pertinent to debugging. The module's
      scope it too wide for that.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Ensuring validation results are communicated are sent to clients is an integrity feature.

# SECTION 6 - Feature Delivery Mechanism:
  1. Verify existing entities meet minimum requirements for use in the system.
  2. A description of an error condition, boundary violation, experienced or caused by an entity in
      the validation domain.
  3. The root of a scalable, modular hierarchy for validation related exceptions.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`

# SECTION 8 - Contains:
  * `ValidationException`
"""

from chess.system import NullException, ValidationException, BlankStringException


__all__ = [
  'NullNameException',
  'LongNameException',
  'ShortNameException',
  'BlankNameException',
  'InvalidNameException',
]


class InvalidNameException(ValidationException):
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

