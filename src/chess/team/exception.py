from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'TeamException',
    'TeamRollBackException',

# === TEAM VALIDATION EXCEPTIONS ===
    'NullTeamException',
    'InvalidTeamException',

# === TEAM BUILDER EXCEPTIONS ===
    'TeamBuilderException',
    'NullTeamSchemaException',

# === TEAM MEMBER EXCEPTIONS ===
    'AddTeamMemberException',
    'AddEnemyToRosterException',
    'RemoveTeamMemberException',
    'FullRankQuotaException',

# === TEAM MEMBER EXCEPTIONS WITH ROLLBACK ===
    'AddEnemyHostageRolledBackException',
    'AddTeamMemberRolledBackException',
    'RemoveTeamMemberRolledBackException',
    'FullRankQuotaRolledBackException',

# === HOSTAGE EXCEPTIONS ===
    'InvalidFriendlyHostageException',
    'AddEnemyHostageException',
    'EnemyKingHostageException',
    'HostageRemovalException',

# === HOSTAGE EXCEPTIONS WITH ROLLBACK ===
    'InvalidFriendlyHostageRolledBAckException',
    'AddEnemyToRosterRolledBackException',
    'EnemyKingHostageRolledBackException',
    'HostageRemovalRolledBackException',

# === SEARCH EXCEPTIONS ===
    'RosterNumberOutOfBoundsException'
]

class TeamException(ChessException):
    """
    Super class of all exceptions a Team object raises. Do not use directly. Subclasses give
    details useful for debugging. This class exists primarily to allow catching all team
    exceptions.
    """
    ERROR_CODE = "TEAM_ERROR"
    DEFAULT_MESSAGE = "Team raised an exception."

class TeamRollBackException(TeamException):
    """
    Super class for exceptions that require a rollback to maintain team integrity.
    """
    pass
    ERROR_CODE = "TEAM_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Team raised an exception. Transaction rollback performed."

# === TEAM VALIDATION EXCEPTIONS ===
class NullTeamException(TeamException, NullException):
    """Raised if an entity, method, or operation requires a team but gets null instead."""
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = f"Team cannot be null"

class InvalidTeamException(TeamException, ValidationException):
    """
    Raised by TeamValidator if team fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existing team
    """
    ERROR_CODE = "TEAM_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Team validation failed"
    

# === TEAM BUILDER EXCEPTIONS ===
class TeamBuilderException(TeamException, BuilderException):
    """
    Raised when TeamBuilder encounters an error while building a team. Exists primarily to
    catch all exceptions raised building a new team
    """
    ERROR_CODE = "TEAM_BUILDER_ERROR"
    DEFAULT_MESSAGE = "TeamBuilder raised an exception"

class NullTeamSchemaException(TeamException, NullException):
    """
    Raised if a null TeamProfile is passed to Team.__init__.
    """
    ERROR_CODE = "NULL_SIDE_PROFILE_ERROR"
    DEFAULT_MESSAGE = f"TeamProfile cannot be null"


# === TEAM MEMBER EXCEPTIONS ===
class AddTeamMemberException(TeamException):
    """Raised if piece could not be added to the team's roster"""
    ERROR_CODE = "ADD_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "Could not add piece to team's roster"

class AddEnemyToRosterException(TeamException):
    """Attempting to add an enemy to the team's roster raises an error"""
    ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "An enemy piece cannot be added to the team's roster"

class RemoveTeamMemberException(TeamException):
    """Raised if piece could not be removed from the team's roster"""
    ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "Could not remove a piece to team's roster"

class FullRankQuotaException(TeamException):
    """Raised if the team has not empty slots for the piece's rank."""
    ERROR_CODE = "FULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "The team has no empty slots for the piece's rank"

class ConflictingTeamAssignmentException(TeamException):
    """
    If a piece that's already on one team (piece.team == not None) tries joining
    another InvalidTeamAssignmentException is raised.
    """
    ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR"
    DEFAULT_MESSAGE = "Piece is already assigned to a team."


# === TEAM MEMBER EXCEPTIONS WITH ROLLBACK ===
class AddTeamMemberRolledBackException(TeamRollBackException):
    """
    Raised if a  transaction failed to add a piece could to the team's roster; then the
    transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_TEAM_MEMBER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Adding piece to team's roster failed. Transaction rollback performed."
    )

class AddEnemyToRosterRolledBackException(TeamRollBackException):
    """
    Raised if a transaction attempted to add an enemy to the team's roster.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
       "Caught attempt to add an enemy piece to the team's roster Transaction "
       "rollback performed."
    )

class RemoveTeamMemberRolledBackException(TeamRollBackException):
    """
    Raised if a  transaction failed to remove a piece from the team's roster. The
    transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Could not remove a piece from the team's roster. Transaction rollback performed."
    )

class FullRankQuotaRolledBackException(TeamRollBackException):
    """
    Raised if a transaction failed could not add a piece because there were no empty slots
    for the piece's rank. The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "FULL_RANK_QUOTA_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "The team has no empty slots for the piece's rank. Transaction rollback performed."
    )

class ConflictingTeamAssignmentRolledBackException(TeamRollBackException):
    """
    Raised if a transaction tries to assign a piece to a different team's roster.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Piece is already assigned to a team. Transaction rollback performed."
    )

# === HOSTAGE EXCEPTIONS ===
class InvalidFriendlyHostageException(TeamException):
    """Attempting to a friendly to the hostage list raises an error"""
    ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageException(TeamException):
    """Raised if a piece could not be added to the team's hostage list"""
    ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list"

class EnemyKingHostageException(TeamException):
    """Attempting to an enemy king to the hostage list raises an error"""
    ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be added to the team's hostage list. Kings can only "
        "be checked or checkmated"
    )

class HostageRemovalException(TeamException):
    """Attempting to remove an enemy from the hostage list raises an error"""
    ERROR_CODE = "HOSTAGE_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "An enemy piece cannot be removed from the team's hostage list"


# === HOSTAGE EXCEPTIONS WITH ROLLBACK ===
class InvalidFriendlyHostageRolledBAckException(TeamRollBackException):
    """
    Raised if a transaction attempts to add a friendly piece to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageRolledBackException(TeamRollBackException):
    """
    Raised if a transaction could not add an enemy piece to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list"


class EnemyKingHostageRolledBackException(TeamRollBackException):
    """
    Raised if a transaction attempted adding an enemy king to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be added to the team's hostage list. Kings can only "
        "be checked or checkmated"
    )

class HostageRemovalRolledBackException(TeamRollBackException):
    """
    Raised if a transaction attempted removing an enemy from the hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "HOSTAGE_REMOVAL_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "An enemy piece cannot be removed from the team's hostage list"

# === SEARCH EXCEPTIONS ===
class RosterNumberOutOfBoundsException(TeamException, SearchException):
    """Attempting to search for a roster number < 1 or > team_size raises an error"""
    ERROR_CODE = "ROSTER_NUMBER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Roster numbers are in the range [1, team_size]. Search failed"
    





