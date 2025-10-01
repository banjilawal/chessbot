from chess.exception import ChessException, ValidationException, NullException

__all__ = [
    'TransactionException',
    'EventException',
    'DirectiveException',
    'InvalidDirectiveException',
    'InvalidCaptureContextException',

    'FriendlyFireException',
    'AttackOnEmptySquareException',
    'EnemyNotOnBoardException',
    'NonCombatantTargetException',
    'KingTargetException',
    'AlreadyCapturedException',
    'MissingFromRosterException',
    'HostageTransferConflictException',
    'AutoCaptureException',


    'NullTransactionException',
    'NullEventException',
    'NullDirectiveException',
    'NullDirectiveException',
    'NullCaptureContextException',


]

class TransactionException(ChessException):
    ERROR_CODE = "TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Transaction raised an error"



class NullTransactionException(NullException):
    ERROR_CODE = "NULL_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Transaction cannot be null"







class AutoCaptureException(CaptureContextException):
    ERROR_CODE = "NULL_CAPTURE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CaptureContext cannot be null"


class FriendlyFireException(CaptureContextException):
    DEFAULT_CODE = "FRIENDLY_FIRE"
    DEFAULT_MESSAGE = "Attempted to attack a friendly observer; this should not happen."


class AttackOnEmptySquareException(CaptureContextException):
    DEFAULT_CODE = "ATTACK_ON_EMPTY_SQUARE"
    DEFAULT_MESSAGE = "Attempted to attack an empty square; this should not happen."


class EnemyNotOnBoardException(CaptureContextException):
    DEFAULT_CODE = "ENEMY_NOT_ON_BOARD"
    DEFAULT_MESSAGE = "Attempted to capture a observer not present on the board; this should not happen."


class NonCombatantTargetException(CaptureContextException):
    DEFAULT_CODE = "NON_COMBATANT_TARGET"
    DEFAULT_MESSAGE = "Attempted to capture a non-combatant observer; this should not happen."


class KingTargetException(CaptureContextException):
    DEFAULT_CODE = "KING_TARGET"
    DEFAULT_MESSAGE = "Attempted to capture a King observer; this should not happen."


class AlreadyCapturedException(CaptureContextException):
    DEFAULT_CODE = "ALREADY_CAPTURED"
    DEFAULT_MESSAGE = "Attempted to capture a observer that already has a captor; this should not happen."


class MissingFromRosterException(CaptureContextException):
    DEFAULT_CODE = "MISSING_FROM_ROSTER"
    DEFAULT_MESSAGE = "Expected observer not found in its team's roster; this should not happen."


class HostageTransferConflictException(CaptureContextException):
    DEFAULT_CODE = "HOSTAGE_TRANSFER_CONFLICT"
    DEFAULT_MESSAGE = "Piece already recorded in captor's hostage list; this should not happen."

