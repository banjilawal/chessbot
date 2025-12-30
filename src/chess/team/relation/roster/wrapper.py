# src/chess/team/relation/roster/wrapper.py

"""
Module: chess.team.relation.roster.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_MEMBER_RELATION_TEST_FAILURE EXCEPTION #======================#
    "RosterTokenRelationTestFailedException",
]

from chess.system import RelationTestFailedException


# ======================# TEAM_MEMBER_RELATION_TEST_FAILURE EXCEPTION #======================#
class RosterTokenRelationTestFailedException(RelationTestFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the team-member relationship
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
    ERROR_CODE = "TEAM_MEMBER_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "TeamMemberRelationTest failed."