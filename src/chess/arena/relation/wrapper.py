__all__ = [
    # ======================# ARENA_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
    "ArenaTeamRelationTestFailedException",
]

from chess.system import RelationTestFailedException


# ======================# ARENA_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
class ArenaTeamRelationTestFailedException(RelationTestFailedException):
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