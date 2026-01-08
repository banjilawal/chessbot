# src/chess/team/hostage/wrapper.py

"""
Module: chess.team.hostage.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_RELATION_TEST_FAILURE EXCEPTION #======================#
    "HostageRelationAnalysisFailedException",
]

from chess.system import RelationAnalysisFailedException


# ======================# HOSTAGE_RELATION_TEST_FAILURE EXCEPTION #======================#
class HostageRelationAnalysisFailedException(RelationAnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the team-hostage relationship
        status has been evaluated.

    # PARENT:
        *   ExceptionWrapper

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "TeamHostageRelationTest failed."