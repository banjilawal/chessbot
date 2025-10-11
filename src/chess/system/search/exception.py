# src/chess/system/validate/exception.py

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
See the list of exceptions in the `__all__` list following (e.g., `SearchException`,
`SearchParamException`, `RowAboveBoundsException`).
  * `SearchException`
  * `SearchParamException`
  * `ImpossibleFatalResultException`
"""

from chess.system import ChessException

__all__ = [
  'SearchException',
  'SearchParamException',
  'ImpossibleFatalResultException'
]

class SearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an exception."


class SearchParamException(SearchException):
  """
  This is different from failed validation checks. Might not be
  necessary.
  """
  DEFAULT_CODE = "SEARCH_PARAM_ERROR"
  DEFAULT_MESSAGE = "Search parameters raised an exception."


class ImpossibleFatalResultException(SearchException):
  """
  This is for sanity checking. Events and transactions need to ensure
  an `actor` and the `resource` they need to run team `Transaction` exist
  in the datapool in `SearchContext`. Validations and builds guarantee
  resources and actors exist in the game. If they are not found that
  indicates data inconsistency or nonexistent data pool.
  """
  DEFAULT_CODE = "IMPOSSIBLE_FATAL_RESULT_ERROR"
  DEFAULT_MESSAGE = (
    "The search result should be impossible. The result "
    "indicates team major data inconsistency or system error"
  )








