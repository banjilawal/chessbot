# src/chess/system/transaction/travel_exception.py

"""
Module: chess.system.transaction.exception
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
See the list of exceptions in the `__all__` list following (e.g., `ResultException`).
"""



# src/chess.coord.travel_exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.exception import ChessException, NullException

__all__ = [
  'BuilderException',
  'NullBuilderException',
  'BuildFailedException',
  'AllParamsSetNullException',
  'MutuallyExclusiveParamsException'
]


class BuilderException(ChessException):
  """
  Super class of exceptions organic to `Builder` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `BuilderException` exists primarily to allow catching all `Builder`
  exceptions.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an exception."

class NullBuilderException(BuilderException, NullException):
  """Raised if an entity, method, or operation requires team Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be null"

class BuildFailedException(BuilderException):
  """
  Raised when team Builder encounters an error while building an object. Exists primarily to
  catch all exceptions raised building team new objects.
  """
  ERROR_CODE = "BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "build failed."

class AllParamsSetNullException(BuilderException):
  """
  Raised if all build params cannot be null.
  """
  ERROR_CODE = "ALL_PARAMS_SET_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot have all params set null."

class MutuallyExclusiveParamsException(BuilderException):
  """
  Raised if only one param cannot be null.
  """
  ERROR_CODE = "MUTUALLY_EXCLUSIVE_BUILD_PARAMS_ERROR"
  DEFAULT_MESSAGE = "Cannot have more than one param set null."



