from chess.event import OccupationEventException
from chess.transaction import TransactionException, NullTransactionException
from chess.exception import NullException, ValidationException, BuilderException

__all__ = [
#=== SCAN_TRANSACTION EXCEPTIONS ===
  'ScanTransactionException',
  'NullScanTransactionException',

#=== SCAN_EVENT EXCEPTIONS ===
  'ScanEventException',
  'InvalidScanEventException',
  'NullScanEventException',

#=== SCAN_EVENT BUILD EXCEPTIONS ===
  'ScanEventBuilderException',
  'ScanSubjectException',
]

#=== SCAN TRANSACTION EXCEPTIONS ===
class ScanTransactionException(TransactionException):
  """
  Wraps any ScanEventExceptions or other errors raised during
  the scan's lifecycle.
  """
  ERROR_CODE = "SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "ScanTransaction raised an exception."

class NullScanTransactionException(NullTransactionException):
  """
  Raised by methods, entities, and models that require a ScanTransaction
  but receive a null.
  """
  ERROR_CODE = "NULL_SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "ScanTransaction cannot be null."


#=== SCAN_EVENT EXCEPTIONS ===
class ScanEventException(OccupationEventException):
  """
  Superclass for all scan event exceptions. DO NOT USE DIRECTLY. Subclasses
  give more specific error messages useful for debugging.
  """
  ERROR_CODE = "SCAN_EVENT_ERROR"
  DEFAULT_MESSAGE = "ScanEvent failed validate"


#=== SCAN_EVENT VALIDATION EXCEPTIONS ===
class NullScanEventException(ScanEventException, NullException):
  """Raised by methods, entities, and models that require a ScanEvent but receive a null."""
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "ScanEvent cannot be null"

class InvalidScanEventException(ScanEventException, ValidationException):
  """Raised by ScanEventValidators if validate fails."""
  ERROR_CODE = "SCAN_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "ScanEvent failed validate"


#=== SCAN_EVENT BUILD EXCEPTIONS ===
class ScanEventBuilderException(ScanEventException, BuilderException):
  """Raised when a ScanEventBuilder fails to build a ScanEvent."""
  ERROR_CODE = "SCAN_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "ScanEventBuilder failed to create a ScanEvent"

class ScanSubjectException(ScanEventException):
  """
  Raised if an Scan target is not a friendly or enemy king.
  """
  ERROR_CODE = "SCAN_SUBJECT_ERROR"
  DEFAULT_MESSAGE = "Scan enemy must be a friendly or enemy king"







