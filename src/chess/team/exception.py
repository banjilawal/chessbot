from chess.exception import ChessException, NullException, ValidationException, BuilderException, RollbackException

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
    'TeamRosterException',
    'AddTeamMemberException',
    'AddEnemyToRosterException',
    'RemoveTeamMemberException',
    'FullRankQuotaException',

# === TEAM MEMBER EXCEPTIONS WITH ROLLBACK ===
    'TeamRosterRollBackException',
    'AddEnemyHostageRolledBackException',
    'AddTeamMemberRolledBackException',
    'RemoveTeamMemberRolledBackException',
    'FullRankQuotaRolledBackException',

# === HOSTAGE EXCEPTIONS ===
    'TeamHostageListException',
    'InvalidFriendlyHostageException',
    'AddEnemyHostageException',
    'AddEnemyKingHostageException',
    'HostageRemovalException',

# === HOSTAGE EXCEPTIONS WITH ROLLBACK ===
    'TeamHostageListRolledBackException',
    'InvalidFriendlyHostageRolledBackException',
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


# === TEAM MEMBER LIST EXCEPTIONS ===
class TeamRosterException(TeamException):
    """Raised for errors on team's roster"""
    ERROR_CODE = "TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Team roster raised an exception"


class AddTeamMemberException(TeamRosterException):
    """Raised if piece could not be added to the team's roster"""
    ERROR_CODE = "ADD_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "Could not add piece to team's roster"

class AddEnemyToRosterException(TeamRosterException):
    """Attempting to add an enemy to the team's roster raises an error"""
    ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR"
    DEFAULT_MESSAGE = "An enemy piece cannot be added to the team's roster"

class RemoveTeamMemberException(TeamRosterException):
    """Raised if piece could not be removed from the team's roster"""
    ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "Could not remove a piece to team's roster"

class FullRankQuotaException(TeamRosterException):
    """Raised if the team has not empty slots for the piece's rank."""
    ERROR_CODE = "FULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "The team has no empty slots for the piece's rank"

class ConflictingTeamAssignmentException(TeamRosterException):
    """
    If a piece that's already on one team (piece.team == not None) tries joining
    another InvalidTeamAssignmentException is raised.
    """
    ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR"
    DEFAULT_MESSAGE = "Piece is already assigned to a team."


# === TEAM MEMBER LIST  EXCEPTIONS WITH ROLLBACK ===
class TeamRosterRollBackException(TeamRosterException, RollbackException):
    """Raised for errors on team's roster that are raised after rollback."""
    ERROR_CODE = "TEAM_ROSTER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Team roster raised an exception. Transaction rollback performed."

class AddTeamMemberRolledBackException(TeamRosterRollBackException):
    """
    Raised if a  transaction failed to add a piece could to the team's roster; then the
    transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_TEAM_MEMBER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Adding piece to team's roster failed. Transaction rollback performed."
    )

class AddEnemyToRosterRolledBackException(TeamRosterRollBackException):
    """
    Raised if a transaction attempted to add an enemy to the team's roster.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_TO_ROSTER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
       "Caught attempt to add an enemy piece to the team's roster Transaction "
       "rollback performed."
    )

class RemoveTeamMemberRolledBackException(TeamRosterRollBackException):
    """
    Raised if a  transaction failed to remove a piece from the team's roster. The
    transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "REMOVE_TEAM_MEMBER_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Could not remove a piece from the team's roster. Transaction rollback performed."
    )

class FullRankQuotaRolledBackException(TeamRosterRollBackException):
    """
    Raised if a transaction failed could not add a piece because there were no empty slots
    for the piece's rank. The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "FULL_RANK_QUOTA_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "The team has no empty slots for the piece's rank. Transaction rollback performed."
    )

class ConflictingTeamAssignmentRolledBackException(TeamRosterRollBackException):
    """
    Raised if a transaction tries to assign a piece to a different team's roster.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "CONFLICTING_TEAM_ASSIGNMENT_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Piece is already assigned to a team. Transaction rollback performed."
    )

# === HOSTAGE LIST EXCEPTIONS ===
class TeamHostageListException(TeamException):
    """Raised on errors with team's hostage list"""
    ERROR_CODE = "TEAM_HOSTAGE_LIST_ERROR"
    DEFAULT_MESSAGE = "Team hostage list raised an exception"

class InvalidFriendlyHostageException(TeamHostageListException):
    """Attempting to a friendly to the hostage list raises an error"""
    ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageException(TeamHostageListException):
    """Raised if a piece could not be added to the team's hostage list"""
    ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list"

class AddEnemyKingHostageException(TeamHostageListException):
    """Attempting to an enemy king to the hostage list raises an error"""
    ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be added to the team's hostage list. Kings can only "
        "be checked or checkmated"
    )

class HostageRemovalException(TeamHostageListException):
    """Attempting to remove an enemy from the hostage list raises an error"""
    ERROR_CODE = "HOSTAGE_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "An enemy piece cannot be removed from the team's hostage list"


# === HOSTAGE LIST EXCEPTIONS WITH ROLLBACK ===
class TeamHostageListRolledBackException(TeamHostageListException, RollbackException):
    """
    Raised on transactions that raise hostage list errors. Exception is raised after
    the transaction is rolled back.
    """
    ERROR_CODE = "TEAM_HOSTAGE_LIST_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Team hostage list raised an exception. Transaction rollback performed."
    )

class InvalidFriendlyHostageRolledBackException(TeamHostageListRolledBackException):
    """
    Raised if a transaction attempts to add a friendly piece to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "INVALID_FRIENDLY_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "A friendly piece cannot be added to the team's hostage list"

class AddEnemyHostageRolledBackException(TeamHostageListRolledBackException):
    """
    Raised if a transaction could not add an enemy piece to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Could not add an enemy piece to the team's hostage list"


class EnemyKingHostageRolledBackException(TeamHostageListRolledBackException):
    """
    Raised if a transaction attempted adding an enemy king to the team's hostage list.
    The transaction was rolled back before raising this exception.
    """
    ERROR_CODE = "ADD_ENEMY_KING_HOSTAGE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be added to the team's hostage list. Kings can only "
        "be checked or checkmated"
    )

class HostageRemovalRolledBackException(TeamHostageListRolledBackException):
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
    





