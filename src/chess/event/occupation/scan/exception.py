from chess.event import OccupationEventException
from chess.piece import InvalidPieceException
from chess.exception import NullException, ValidationException

__all__ = [
    'ScanEventException',
    'InvalidScanEventException',
    'NullScanEventException',
    'InvalidScanSubjectException',
]

class ScanEventException(OccupationEventException):
    """
    Superclass for all scan event exceptions. DO NOT USE DIRECTLY. Subclasses give more specific error messages
    useful for debugging.
    """
    ERROR_CODE = "SCAN_EVENT_ERROR"
    DEFAULT_MESSAGE = "ScanEvent failed validation"

class NullScanEventException(ScanEventException, NullException):
    """Raised by methods, entities, and models that require a ScanEvent but receive a null."""
    ERROR_CODE = "NULL_EVENT_ERROR"
    DEFAULT_MESSAGE = "ScanEvent cannot be null"


class InvalidScanEventException(ScanEventException, ValidationException):
    """Raised by ScanEventValidators if validation fails."""
    ERROR_CODE = "SCAN_EVENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "ScanEvent failed validation"


class ScanEventBuilderException(ScanEventException):
    """Raised when a ScanEventBuilder fails to build a ScanEvent."""
    ERROR_CODE = "SCAN_EVENT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScanEventBuilder failed to create a ScanEvent"


class InvalidScanSubjectException(ScanEventException, InvalidPieceException):
    """Raised if a subject of a scan is invalid."""
    ERROR_CODE = "SCAN_SUBJECT_ERROR"
    DEFAULT_MESSAGE = "Subject of ScanEvent failed validation. Scan cannot be executed"


