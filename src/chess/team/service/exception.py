# src/chess/team/service/base.py

"""
Module: chess.team.entity_service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ======================# TEAM_SERVICE EXCEPTIONS #======================#
    "TeamServiceException",
]

# ======================# TEAM_SERVICE EXCEPTIONS #======================#
class TeamServiceException(ServiceException):
    """wrapper for exceptions which hit a TeamCertifier method's finally block."""
    ERROR_CODE = "TEAM_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "TeamCertifier raised an exception."