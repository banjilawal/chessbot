# src/chess/dyad/service/exception.py

"""
Module: chess.dyad.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.dyad import SchemaAgentPairException

class SchemaAgentPairServiceException(SchemaAgentPairException, ServiceException):
    pass


from chess.system import ServiceException
from chess.dyad import SchemaAgentPairException

__all__ = [
    # ======================# SCHEMA_AGENT_PAIR_SERVICE EXCEPTION #======================#
    "SchemaAgentPairServiceException",
]


# ======================# SCHEMA_AGENT_PAIR_SERVICE EXCEPTION #======================#
class SchemaAgentPairServiceException(SchemaAgentPairException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaAgentPairService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaAgentPairService method.

    # PARENT:
        *   ServiceException
        *   SchemaAgentPairException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_AGENT_PAIR_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SchemaAgentPairService raised an exception."