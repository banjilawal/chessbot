from chess.operation.occupation import OccupationException

__all__ = [
    'AttackException',

    # Specific attack errors (no rollback)
    'UnexpectedNullEnemyException',


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
    DEFAULT_MESSAGE = "Target observer is unexpectedly null during capture; this should not happen."





# --- Rollback Attack Errors (Dual Inheritance) ---

class RosterRemovalRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove observer from enemy roster after assigning captor; rollback performed."


class HostageAdditionRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to add captured observer to captor's hostage list; rollback performed."


class BoardPieceRemovalRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove captured observer from board; rollback performed."


class SquareOccupationRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to occupy target square after capture; rollback executed."


class SourceSquareRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."


class PositionUpdateRollbackException(AttackException, RollbackException):
    DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to update observer's position history after move; rollback executed."
