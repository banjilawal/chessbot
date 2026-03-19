# src/logic/arena/relation/worker.py

"""
Module: logic.arena.relation.work
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

__all__ = [
    # ======================# ARENA_TEAM_RELATION_ANALYSIS_FAILURE #======================#
    "ArenaTeamAnalysisException",
]

from logic.system import AnalysisException


# ======================# ARENA_TEAM_RELATION_ANALYSIS_FAILURE #======================#
class ArenaTeamAnalysisException(AnalysisException):
    """
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the arena-team relationship
        status has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_TEAM_RELATION_ANALYSIS_FAILURE"
    MSG = "ArenaTeamRelationTest failed."