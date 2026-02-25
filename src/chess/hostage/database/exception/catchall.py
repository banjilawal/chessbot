# src/chess/hostage/database/exception/catchall.py

"""
Module: chess.hostage.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# HOSTAGE_DIRECTORY_SERVICE EXCEPTION #======================#
    "HostageDatabase",
]

from chess.hostage import HostageException
from chess.system import DatabaseException


# ======================# HOSTAGE_DIRECTORY_SERVICE EXCEPTION #======================#
class HostageDatabaseException(HostageException, DatabaseException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an HostageDatabase encountered an error which prevented the
        service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a HostageDatabase method.

    # PARENT:
        *   ServiceException
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_DIRECTORY_SERVICE_ERROR"
    MSG = "HostageDatabase raised an exception."