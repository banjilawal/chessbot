# src/chess/system/event/exception.py

"""
Module: chess.system.event.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the exception being raised.
       `IdValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying ids.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""

# src/chess/vector/exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""
from chess.event import OccupationEventException
from chess.transaction import TransactionException, NullTransactionException
from chess.exception import NullException, ValidationException, BuilderException

__all__ = [
#=== SCAN_TRANSACTION EXCEPTIONS #======================#  
  'ScanTransactionException',
  'NullScanTransactionException',

#=== SCAN_EVENT EXCEPTIONS #======================#  
  'ScanEventException',
  'InvalidScanEventException',
  'NullEncounterEventException',

#=== SCAN_EVENT BUILD EXCEPTIONS #======================#  
  'ScanEventBuilderException',
  'ScanSubjectException',
]

#=== SCAN TRANSACTION EXCEPTIONS #======================#  
class ScanTransactionException(TransactionException):
  """
  Wraps any ScanEventExceptions or other errors raised during
  the encounter's lifecycle.
  """
  ERROR_CODE = "SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "OccupationTransaction raised an exception."

class NullScanTransactionException(NullTransactionException):
  """
  Raised by methods, entities, and models that require team OccupationTransaction
  but receive team null.
  """
  ERROR_CODE = "NULL_SCAN_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "OccupationTransaction cannot be null."


#=== SCAN_EVENT EXCEPTIONS #======================#  
class ScanEventException(OccupationEventException):
  """
  Superclass for all encounter event exceptions. DO NOT USE DIRECTLY. Subclasses
  give more specific error messages useful for debugging.
  """
  ERROR_CODE = "SCAN_EVENT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent failed validate"


#=== SCAN_EVENT VALIDATION EXCEPTIONS #======================#  
class NullEncounterEventException(ScanEventException, NullException):
  """Raised by methods, entities, and models that require team EncounterEvent but receive team null."""
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent cannot be null"

class InvalidScanEventException(ScanEventException, ValidationException):
  """Raised by ScanEventValidators if validate fails."""
  ERROR_CODE = "SCAN_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent failed validate"


#=== SCAN_EVENT BUILD EXCEPTIONS #======================#  
class ScanEventBuilderException(ScanEventException, BuilderException):
  """Raised when team ScanEventBuilder fails to build team EncounterEvent."""
  ERROR_CODE = "SCAN_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "ScanEventBuilder failed to create team EncounterEvent"

class ScanSubjectException(ScanEventException):
  """
  Raised if an Scan target is not team friendly or enemy king.
  """
  ERROR_CODE = "SCAN_SUBJECT_ERROR"
  DEFAULT_MESSAGE = "Scan enemy must be team friendly or enemy king"







