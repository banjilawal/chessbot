from chess.exception import RollbackException
from chess.event.occupation import OccupationEventException

__all__ = [
    'AttackEventException',

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


class AttackEventException(OccupationEventException):
    """
    Base class for exceptions raised during attack/capture operations.

    PURPOSE:
        Used when an error occurs in the course of an attack or capture
        (e.g., invalid target, rollback during capture, inconsistent board state).
    """
    DEFAULT_CODE = "ATTACK_ERROR"
    DEFAULT_MESSAGE = "An error occurred during an attack or capture transaction."

# --- Specific Attack Errors (No Rollback) ---

class UnexpectedNullEnemyException(AttackEventException):
    DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
    DEFAULT_MESSAGE = "Target actor is unexpectedly null during capture; this should not happen."





# --- Rollback Attack Errors (Dual Inheritance) ---
class SetCaptorRollBackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."

class RosterRemovalRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove actor from enemy roster after assigning captor; rollback performed."


class HostageAdditionRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to add captured actor to captor's hostage list; rollback performed."


class BoardPieceRemovalRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to remove captured actor from board; rollback performed."


class SquareOccupationRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to occupy target square after capture; rollback executed."


class SourceSquareRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."


class PositionUpdateRollbackException(AttackEventException, RollbackException):
    DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
    DEFAULT_MESSAGE = "Failed to update actor's position history after move; rollback executed."
