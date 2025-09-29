from chess.exception import ChessException, ValidationException, NullException

__all__ = [
    'OperationException',
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


    'NullOperationException',
    'NullEventException',
    'NullDirectiveException',
    'NullDirectiveException',
    'NullCaptureContextException',


]

class OperationException(ChessException):
    ERROR_CODE = "OPERATION_ERROR"
    DEFAULT_MESSAGE = "Operation raised an error"

class EventException(OperationException):
    ERROR_CODE = "OPERATION_EXECUTOR_ERROR"
    DEFAULT_MESSAGE = "OperationExecutor raised an error"

class DirectiveException(OperationException):
    ERROR_CODE = "DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive raised an error"

class InvalidDirectiveException(ValidationException):
    ERROR_CODE = "INVALID_DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive validation failed"



class NullOperationException(NullException):
    ERROR_CODE = "NULL_OPERATION_ERROR"
    DEFAULT_MESSAGE = "Operation cannot be null"

class NullEventException(EventException, NullOperationException):
    ERROR_CODE = "NULL_OPERATION_EXECUTOR_ERROR"
    DEFAULT_MESSAGE = "OperationExecutor cannot be null"

class NullDirectiveException(NullOperationException):
    ERROR_CODE = "NULL_DIRECTIVE_ERROR"
    DEFAULT_MESSAGE = "Directive cannot be null"

class NullDirectiveValidatorException(NullOperationException):
    ERROR_CODE = "NULL_DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Directive validation failed"




class CaptureContextException(OperationException):
    ERROR_CODE = "CAPTURE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CaptureContext raised an error"

class InvalidCaptureContextException(ValidationException):
    ERROR_CODE = "CAPTURE_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CaptureContext validation failed. Cannot attack"

class NullCaptureContextException(NullOperationException):
    ERROR_CODE = "NULL_CAPTURE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CaptureContext cannot be null"


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

