from chess.team import InvalidTeamException
from chess.system import RegistrationException

__all__ = [
    # ======================# TEAM_REGISTRATION EXCEPTIONS #======================#  
    "TeamRegistrationException",
    "TeamNotRegisteredWithActorException",
]


# ======================# TEAM_REGISTRATION EXCEPTIONS #======================#  
class TeamRelationshipException(TeamRelationshipException):
    """
    There is a subtle difference between relationship and registration exceptions.
    There is no collection on the owning side. There is simply a bidirectional relationship
    between two entities and there is no collection involved.
    Relationship exceptions deal with
        *   Temporary occupations (Piece occupying a Square)
        *   One-to-Many where the One side does not have a dataset of the many.
            This is useful for filtering as in directly doing team.game comparisons.
        *   When there is a mismatch between a collection[T] owner and a t instance that belongs
            to a completely different collection[T] instance.
    """
    ERROR_CODE = "TEAM_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "No relationship found with Team."


class NoTeamGameRelastionshipException(TeamRelationshipException):
    """Raised when Team.game != game"""
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_AGENT_ERROR"
    DEFAULT_MESSAGE = "There is no relationship between the Game and Team."


class TeamAgentMismatchException(TeamRelationshipException):
    """Raised when Team.agent != agent this is different"""
    ERROR_CODE = "TEAM_MISMATCHES_AGENT_ERROR"
    DEFAULT_MESSAGE = (
        "There is no relationship between the Team and the Agent. The Team says its "
        "registered with a completely different Agent."
    )
