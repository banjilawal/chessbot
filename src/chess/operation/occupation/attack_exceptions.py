from chess.operation.occupation import OccupationException

__all__ = [
    'AttackException',

    # Specific attack errors (no rollback)
    'UnexpectedNullEnemyException',
    'FriendlyFireException',
    'AttackOnEmptySquareException',
    'EnemyNotOnBoardException',
    'NonCombatantTargetException',
    'KingTargetException',
    'AlreadyCapturedException',
    'MissingFromRosterException',
    'HostageTransferConflictException',

    # Rollback attack errors (dual inheritance)
    'RosterRemovalRollbackException',
    'HostageAdditionRollbackException',
    'BoardPieceRemovalRollbackException',
    'SquareOccupationRollbackException',
    'SourceSquareRollbackException',
    'PositionUpdateRollbackException',
]


class AttackException(OccupationException):
    """
    Base class for exceptions raised during attack/capture operations.

    PURPOSE:
        Used when an error occurs in the course of an attack or capture
        (e.g., invalid target, rollback during capture, inconsistent board state).
    """
    DEFAULT_CODE = "ATTACK_ERROR"
    DEFAULT_MESSAGE = "An error occurred during an attack or capture operation."

# --- Specific Attack Errors (No Rollback) ---

class UnexpectedNullEnemyException(AttackException):
    DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
    DEFAULT_MESSAGE = "Target piece is unexpectedly null during capture; this should not happen."


class FriendlyFireException(AttackException):
    DEFAULT_CODE = "FRIENDLY_FIRE"
    DEFAULT_MESSAGE = "Attempted to attack a friendly piece; this should not happen."


class AttackOnEmptySquareException(AttackException):
    DEFAULT_CODE = "ATTACK_ON_EMPTY_SQUARE"
    DEFAULT_MESSAGE = "Attempted to attack an empty square; this should not happen."


class EnemyNotOnBoardException(AttackException):
    DEFAULT_CODE = "ENEMY_NOT_ON_BOARD"
    DEFAULT_MESSAGE = "Attempted to capture a piece not present on the board; this should not happen."


class NonCombatantTargetException(AttackException):
    DEFAULT_CODE = "NON_COMBATANT_TARGET"
    DEFAULT_MESSAGE = "Attempted to capture a non-combatant piece; this should not happen."


class KingTargetException(AttackException):
    DEFAULT_CODE = "KING_TARGET"
    DEFAULT_MESSAGE = "Attempted to capture a King piece; this should not happen."


class AlreadyCapturedException(AttackException):
    DEFAULT_CODE = "ALREADY_CAPTURED"
    DEFAULT_MESSAGE = "Attempted to capture a piece that already has a captor; this should not happen."


class MissingFromRosterException(AttackException):
    DEFAULT_CODE = "MISSING_FROM_ROSTER"
    DEFAULT_MESSAGE = "Expected piece not found in its team's roster; this should not happen."


class HostageTransferConflictException(AttackException):
    DEFAULT_CODE = "HOSTAGE_TRANSFER_CONFLICT"
    DEFAULT_MESSAGE = "Piece already recorded in captor's hostage list; this should not happen."


# --- Rollback Attack Errors (Dual Inheritance) ---

class RosterRemovalRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove piece from enemy roster after assigning captor; rollback performed."


class HostageAdditionRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to add captured piece to captor's hostage list; rollback performed."


class BoardPieceRemovalRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove captured piece from board; rollback performed."


class SquareOccupationRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to occupy target square after capture; rollback executed."


class SourceSquareRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."


class PositionUpdateRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to update piece's position history after move; rollback executed."
