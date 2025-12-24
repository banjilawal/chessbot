__all__ = [
    # ======================# RANK_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "RankContextBuildFailedException",
]


# ======================# RANK_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class RankContextBuildFailedException(RankContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the RankContext build creates an exception. Failed check exceptions are encapsulated
        in an RankContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The RankContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   RankContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "RankContext build failed."