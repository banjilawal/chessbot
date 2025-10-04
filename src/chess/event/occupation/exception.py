from chess.event import EventException, EventBuilderException
from chess.exception import ValidationException, NullException, BuilderException


#
# __all__ = [
#     'TeamException',
#     'TeamRollBackException',
#
#     # === TEAM VALIDATION EXCEPTIONS ===
#     'NullTeamException',
#     'InvalidTeamException',
#
#
#
#     'TeamBuilderException',
#     'NullTeamSchemaException',
#
#     # === TEAM MEMBER EXCEPTIONS ===
#     'TeamRosterException',
#     'AddTeamMemberException',
#     'AddEnemyToRosterException',
#     'RemoveTeamMemberException',
#     'FullRankQuotaException',
#
#     # === TEAM MEMBER EXCEPTIONS WITH ROLLBACK ===
#     'TeamRosterRollBackException',
#     'AddEnemyHostageRolledBackException',
#     'AddTeamMemberRolledBackException',
#     'RemoveTeamMemberRolledBackException',
#     'FullRankQuotaRolledBackException',
#
#     # === HOSTAGE EXCEPTIONS ===
#     'TeamHostageListException',
#     'InvalidFriendlyHostageException',
#     'AddEnemyHostageException',
#     'AddEnemyKingHostageException',
#     'HostageRemovalException',
#
#     # === HOSTAGE EXCEPTIONS WITH ROLLBACK ===
#     'TeamHostageListRolledBackException',
#     'InvalidFriendlyHostageRolledBackException',
#     'AddEnemyToRosterRolledBackException',
#     'EnemyKingHostageRolledBackException',
#     'HostageRemovalRolledBackException',
#
#     # === SEARCH EXCEPTIONS ===
#     'RosterNumberOutOfBoundsException'
# ]

__all__ = [
    'OccupationEventException',

    # === OccupationEvent VALIDATION EXCEPTIONS ===
    'InvalidOccupationEventException',
    'NullOccupationEventException',
    'CircularOccupationException',
    'TargetSquareMismatchException',

    # === OccupationEvent BUILDER EXCEPTIONS ===
    'OccupationEventBuilderException'
    
    
    # 'HostageValidationEventException',
    # 'NullHostagePieceEventException',
    # 'InvalidOccupationEventException',
    # 'OccupationSearchEventException',
]

class OccupationEventException(EventException):
    ERROR_CODE = "OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "An err was raised while executing the square occupation"

# === OccupationEvent VALIDATION EXCEPTIONS ===
class NullOccupationEventException(OccupationEventException, NullException):
    ERROR_CODE = "NULL_OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "OccupationEvent cannot be null"

class InvalidOccupationEventException(OccupationEventException, ValidationException):
    """OccupationEvent validate failure."""
    ERROR_CODE = "OCCUPATION_EVENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "OccupationEvent failed validate"

class CircularOccupationException(OccupationEventException):
    ERROR_CODE = "CIRCULAR_OCCUPATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already occupying the destination square"

class TargetSquareMismatchException(OccupationEventException):
    """
    Raised if a target's square does not match. destination_square
    """
    ERROR_CODE = "TARGET_SQUARE_MISMATCH_ERROR"
    DEFAULT_MESSAGE = "Target piece is at a different square from expected."

class ActorSquareNotFoundException(OccupationEventException):
    ERROR_CODE = "ACTOR_SQUARE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = (
        "The validated actor with a current could not find its square in BoardSearch"
    )


# === OccupationEvent BUILDER EXCEPTIONS ===
class OccupationEventBuilderException(OccupationEventException, BuilderException):
    ERROR_CODE = "OCCUPATION_EVENT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "OccupationEventBuilder failed to create an OccupationEvent."

#
#
#
# class HostageValidationEventException(OccupationEventException):
#     ERROR_CODE = "HOSTAGE_VALIDATION_ERROR"
#     DEFAULT_MESSAGE = f"Hostage validate failed"
#
#
# class NullHostagePieceEventException(OccupationEventException):
#     """
#     Raised if a enemy is null. Parent class for:
#         - NullCombatantPieceException
#         - NullKingException
#     Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
#     Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
#     """
#
#     ERROR_CODE = "NULL_PIECE_ERROR"
#     DEFAULT_MESSAGE = f"Piece cannot be null"
#
#
# class NullCombatantPieceEventException(OccupationEventException):
#     """
#     Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
#     """
#
#     ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
#     DEFAULT_MESSAGE = f"CombatantPiece cannot be null"
#
#
# class OccupationSearchEventException(OccupationEventException):
#     """
#     Board searches during an occupation should not fai. If they do there is an inconsistency in the board
#     """
#
#     ERROR_CODE = "OCCUPATION_SEARCH_ERROR"
#     DEFAULT_MESSAGE = f"BoardSearch failed to find a square; this should not happen in an occupation operation"