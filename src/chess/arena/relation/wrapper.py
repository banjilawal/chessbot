# src/chess/arena/relation/wrapper.py

"""
Module: chess.arena.relation.wrapper
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_TEAM_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "ArenaTeamAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# ARENA_TEAM_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class ArenaTeamAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the arena-team relationship
        status has been evaluated.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ARENA_TEAM_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "ArenaTeamRelationTest failed."