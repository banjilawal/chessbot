# src/chess/system/event/exception.py

"""
Module: chess.system.event.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import TransactionException

"""
=============================================================================================================#
==============LOG_ENCOUNTER_TRANSACTION EXCEPTIONS ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES=================#
=============================================================================================================#
"""

__all__ = [
  'LogEncounterTransactionException',
  'FailedEncounterAdditionRolledBackException',
]

class LogEncounterTransactionException(TransactionException):
  """"""
  ERROR_CODE = "LOG_ENCOUNTER_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = (
    "LogEncounterTransaction raised an exception. The transaction was rolled back before this exception "
    "was raised."
  )

class FailedEncounterAdditionRolledBackException(LogEncounterTransactionException):
  """"""
  ERROR_CODE = "FAILED_ENCOUNTER_ADDITION_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Adding a new discovery during an encounter-logging transaction failed. The transaction was rolled back before "
    "this exception was raised."
  )



# ======================# ROLLED BACK ATTACK TRANSACTION EXCEPTIONS #======================#

#=== ENCOUNTER_EVENT_EVENT EXCEPTIONS #======================#  
class EncounterEventEventException(OccupationEventException):
  """
  Superclass for all encounter event exceptions. DO NOT USE DIRECTLY. Subclasses
  give more specific error messages useful for debugging.
  """
  ERROR_CODE = "ENCOUNTER_EVENT_EVENT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent failed validate"


#=== ENCOUNTER_EVENT_EVENT VALIDATION EXCEPTIONS #======================#  
class NullEncounterEventException(EncounterEventEventException, NullException):
  """Raised by methods, entities, and models that require team EncounterEvent but receive team null."""
  ERROR_CODE = "NULL_EVENT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent cannot be null"

class InvalidEncounterEventEventException(EncounterEventEventException, ValidationException):
  """Raised by EncounterEventEventValidators if validate fails."""
  ERROR_CODE = "ENCOUNTER_EVENT_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent failed validate"


#=== ENCOUNTER_EVENT_EVENT BUILD EXCEPTIONS #======================#  
class EncounterEventEventBuilderException(EncounterEventEventException, BuilderException):
  """Raised when team EncounterEventBuilder fails to build team EncounterEvent."""
  ERROR_CODE = "ENCOUNTER_EVENT_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "EncounterEventBuilder failed to create team EncounterEvent"

class EncounterEventSubjectException(EncounterEventEventException):
  """
  Raised if an EncounterEvent target is not team friendly or enemy king.
  """
  ERROR_CODE = "ENCOUNTER_EVENT_SUBJECT_ERROR"
  DEFAULT_MESSAGE = "EncounterEvent enemy must be team friendly or enemy king"







