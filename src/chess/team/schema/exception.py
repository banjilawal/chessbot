# src/chess/team_name/schema/exception.py

"""
Module: chess.team_name.schema.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of `TeamSchema` objects.

***Limitations***: It does not contain any logic for raising these exceptions; that responsibility
    `TeamSchema`, `TeamSchemaBuilder`, and `TeamSchemaValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `TeamSchema` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `TeamSchema` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `TeamSchema` graph.
4. Providing a clear distinction between errors related to `TeamSchema` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:

From `chess.system`:
  * Exceptions: `ValidationException`, `NullException`

From `chess.team_name`:
  * `TeamException`:

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `TeamSchemaException`,
`NullTeamSchemaException`, `InvalidTeamSchemaException`, ).
"""

from chess.team import TeamException
from chess.system import NullException, ValidationException


__all__ = [
  'TeamSchemaException',

#======================# TEAM_SCHEMA VALIDATION EXCEPTIONS #======================#
  'NullTeamSchemaException',
  'InvalidTeamSchemaException'
]


class TeamSchemaException(TeamException):
  """
  Super class of all exceptions `TeamSchema` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `TeamSchema`
  exceptions.
  """
  ERROR_CODE = "TEAM_SCHEMA_ERROR"
  DEFAULT_MESSAGE = "TeamSchema raised an rollback_exception."


#======================# TEAM_SCHEMA VALIDATION EXCEPTIONS #======================#
class NullTeamSchemaException(TeamSchemaException, NullException):
  """Raised if an entity, method, or operation requires `TeamSchema` but gets null instead."""
  ERROR_CODE = "NULL_TEAM_SCHEMA_ERROR"
  DEFAULT_MESSAGE = "TeamSchema cannot be null"

class InvalidTeamSchemaException(TeamSchemaException, ValidationException):
  """
  Raised by `TeamSchemaValidator` if an object fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing`TeamSchema`.
  """
  ERROR_CODE = "TEAM_SCHEMA_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TeamSchema validation failed."
