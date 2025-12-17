# src/chess/team/schema/service/exception/operation.py

"""
Module: chess.team.schema.service.exception.operation
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import OperationFailedException
from chess.team import TeamSchemaServiceException


__all__ = [
    # ======================# TEAM_SCHEMA_SERVICE_OPERATION_FAILED EXCEPTION #======================#
    "TeamSchemaLookupFailedException",
]

# ======================# TEAM_SCHEMA__SERVICE_OPERATION_FAILED EXCEPTION #======================#
class TeamSchemaLookupFailedException(TeamSchemaServiceException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wraps unhandled exceptions that hit the try-finally block of a TeamSchemaLookup method.

    # PARENT:
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "TeamSchemaLookup operation failed."

