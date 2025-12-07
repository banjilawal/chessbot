# src/chess/team/context/entity_service/base.py

"""
Module: chess.team.context.entity_service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ========================= TEAM_CONTEXT_SERVICE EXCEPTIONS =========================#
    "TeamContextServiceException",
]


# ========================= TEAM_CONTEXT_SERVICE EXCEPTIONS =========================#
class TeamContextServiceException(ServiceException):
    """wrapper for exceptions which hit a TeamContextService method's finally block."""
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService raised an exception."