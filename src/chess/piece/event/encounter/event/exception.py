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


from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'EncounterEventException',

# ======================# ENCOUNTER_EVENT VALIDATION EXCEPTIONS #======================#
  'NullEncounterEventException',
  'PieceEncounteringItSelfException',
  'NUllEncounterSubjectException',
  'DoubleEncounterException',

#======================# ENCOUNTER_EVENT BUILD EXCEPTIONS #======================#
  'EncounterEventBuildFailedException',
]


class EncounterEventException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "ENCOUNTER_EVENT_ERROR"
  DEFAULT_MESSAGE = "An EncounterEvent raised an exception."


#======================# ENCOUNTER_EVENT VALIDATION EXCEPTIONS #======================#
class NullEncounterEventException(EncounterEventException, NullException):
  """
  Raised if an entity, method, or operation requires team piece but gets null instead.
  Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullEncounterException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_ENCOUNTER_EVENT_ERROR"
  DEFAULT_MESSAGE = "Encounter cannot be null"

class PieceEncounteringItSelfException(EncounterEventException):
  """"""
  ERROR_CODE = "PIECE_ENCOUNTERING_ITSELF_ERROR"
  DEFAULT_MESSAGE = "Piece cannot encounter itself."

class NUllEncounterSubjectException(EncounterEventException):
  """"""
  ERROR_CODE = "NULL_ENCOUNTER_SUBJECT_ERROR"
  DEFAULT_MESSAGE = "An EncounterEvent cannot have a null subject."

class DoubleEncounterException(EncounterEventException):
  """"""
  ERROR_CODE = "DOUBLE_ENCOUNTER_ERROR"
  DEFAULT_MESSAGE = "The subject has already been encountered."

class InvalidEncounterException(EncounterEventException, ValidationException):
  """"""
  ERROR_CODE = "INVALID_ENCOUNTER_EVENT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent validation failed."


#======================# ENCOUNTER_EVENT BUILD EXCEPTIONS #======================#
class EncounterEventBuildFailedException(EncounterEventException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "ENCOUNTER_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent build failed."







