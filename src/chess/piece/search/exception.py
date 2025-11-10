# src/chess.visitor_coord.rollback_exception.py

"""
Module: chess.visitor_coord.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exceptions into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

"""
Result exceptions are about `Result` construction not the contents of the notification. A `ResultException` is
raised by `Builder` objects.
"""

from chess.exception import ChessException

__all__ = [
  'ResultException',
  'ResultConstructorException',
  'EmptyResultConstructorException',
  'ErrorContradictsPayloadException'
]

class ResultException(ChessException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_ERROR"
  DEFAULT_MESSAGE = "Result raised an rollback_exception."


class ResultConstructorException(ResultException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "Invalid constructor params raised an rollback_exception."


class EmptyResultConstructorException(ResultConstructorException):
  ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
  """Raised if both payload and error params are not null when constructing team Result object"""
  ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
  DEFAULT_MESSAGE = (
    "A Result cannot have both its payload and error set. Construct with either payload or err"
  )
  
# src/chess/system/old_search/rollback_exception.py

"""
Module: chess.system.old_search.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's effects and actions cover exceptions raised by implementors of the `Search` interface.

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
See the list of exceptions in the `__all__` list following (e.g., `SearchException`,
`SearchParamException`, `RowAboveBoundsException`).
  * `SearchException`
  * `SearchParamException`
  * `ImpossibleFatalResultException`
"""

from chess.system import ChessException, SearchCollisionException

__all__ = [
  'DiscoverySearchException',
  'SearchParamException',
  'ImpossibleFatalResultException',

#======================# SEARCH_COLLISION EXCEPTIONS #======================#
  'DiscoverySearchCollisionException',
  'DiscoverySearchIdCollisionException',
  'DiscoverySearchNameCollisionException',
  'DiscoverySearchCoordCollisionException',

  'SquareSearchIdCollisionException',
  'SquareSearchNameCollisionException',
  'SquareSearchCoordCollisionException',

  'TeamSearchIdCollisionException'
]

class DiscoverySearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an rollback_exception."


#======================# SEARCH_COLLISION EXCEPTIONS #======================#
class DiscoverySearchCollisionException(DiscoverySearchException, SearchCollisionException):
  DEFAULT_CODE = "DISCOVERY_SEARCH_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "DiscoverySearch results contains records with multiple records with properties that should be unique. There "
    "may be service inconsistencies."
  )


class DiscoverySearchIdCollisionException(DiscoverySearchCollisionException):
  DEFAULT_CODE = "DISCOVERY_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "DiscoverySearch results contains has more than one consistency for the piece_id which should be unique. There "
    "may be service inconsistencies."
  )

class DiscoverySearchNameCollisionException(DiscoverySearchCollisionException):
  DEFAULT_CODE = "DISCOVERY_SEARCH_NAME_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "DiscoverySearch results contains has more than one consistency for discovery_name, which should be unique. There "
    "may be service inconsistencies."
  )

class DiscoverySearchCoordCollisionException(DiscoverySearchCollisionException):
  DEFAULT_CODE = "DISCOVERY_SEARCH_COORD_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "DiscoverySearch results contains has more than one consistency for discovery_position, which should be unique. There "
    "may be service inconsistencies."
  )


class SquareSearchIdCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found with the same visitor_id. There may be a service inconsistency."
  )


class SquareSearchNameCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_NAME_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found with the same visitor_name. There may be a service collision"
  )

class SquareSearchCoordCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_COORD_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found at the same coordinate. There may be a service inconsistency."
  )

class TeamSearchIdCollisionException(SearchCollisionException):
  DEFAULT_CODE = "TEAM_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Team found with the same visitor_name. There may be a service inconsistency."
  )












