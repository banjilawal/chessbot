# src/chess/arena/relation/wrapper.py

"""
Module: chess.arena.relation.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
    "ArenaTeamRelationAnalysisFailedException",
]

from chess.system import RelationAnalysisFailedException


# ======================# ARENA_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
class ArenaTeamRelationAnalysisFailedException(RelationAnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the arena-team relationship
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
    ERROR_CODE = "ARENA_TEAM_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "ArenaTeamRelationTest failed."