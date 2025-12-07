# src/chess/system/validate/base.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-04
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
  2. Ensuring coord_stack_validator results are communicated are sent to clients is an integrity feature.

# SECTION 6 - Feature Delivery Mechanism:
  1. Verify existing entities meet minimum requirements for use in the system.
  2. A description of an error condition, boundary violation, experienced or caused by an entity in
      the coord_stack_validator graph.
  3. The root of a scalable, modular hierarchy for coord_stack_validator related exceptions.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`

# SECTION 8 - Contains:
  * `ValidationException`
"""

from chess.system import ChessException





__all__ = [
  # ======================# VALIDATOR EXCEPTION SUPER_CLASS #======================#
  "ValidatorException",
  
  # ======================# VALIDATOR VALIDATION EXCEPTIONS #======================#
  "UnreliableValidatorException",
  "NullValidatorException",
  
  # ======================# FAILED BUILD OPERATION EXCEPTION #======================#
  "BuildFailedException",
  
  # ======================# MUTUAL EXCLUSION EXCEPTIONS #======================#
  "AllParamsSetNullException",
  "MutuallyExclusiveParamsException",
  
  # ======================# BUILD_OPTIONS EXCEPTIONS #======================#
  "NoBuildOptionSelectedException",
  "BuildOptionSelectionTooLargeException",
]


# ======================# VALIDATOR  #======================#
class ValidatorException(ChessException):
  """
  Super class of exceptions organic to Validator objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `ValidatorException` exists primarily to allow catching all `Validator`
  exceptions.
  """
  ERROR_CODE = "VALIDATOR_ERROR"
  DEFAULT_MESSAGE = "Validator raised an exception."


# ======================# VALIDATOR CERTIFICATION EXCEPTIONS #======================#
class UnreliableValidatorException(ValidatorException):
  """Raised if an entity, method, or operation requires team_name Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Validator cannot be validation"


class NullValidatorException(UnreliableValidatorException):
  """Raised if an entity, method, or operation requires team_name Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Validator cannot be validation"


# ======================# ENTITY VALIDATION EXCEPTION #======================#
class ValidationException(ChessException):
  """
  Super class of all errors raised verifying correctness of existing entities. DO NOT USE DIRECTLY. Create or use
  subclasses specific to a class.
  """
  ERROR_CODE = "VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Validation failed."