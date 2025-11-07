# src/chess/owner/travel/attack/travel/rollback_exception.py

"""
Module: chess.owner.travel.attack.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""
from chess.piece import TravelEventException
from chess.system import NullException, ValidationException

__all__ = [
  'CheckEventException',
  'NullCheckEventException',
  'KingCheckingItselfException',
  'InvalidCheckEventException',
]


class CheckEventException(TravelEventException):
  """"""
  ERROR_CODE = "CHECK_ERROR"
  DEFAULT_MESSAGE = "A check event raised an exception."


#======================# ATTACK_EVENT VALIDATION EXCEPTIONS #======================#
class NullCheckEventException(CheckEventException, NullException):
  """"""
  ERROR_CODE = "NULL_CHECK_EVENT_ERROR"
  DEFAULT_MESSAGE = "CheckEvent cannot be null."

class KingCheckingItselfException(CheckEventException):
  """"""
  ERROR_CODE = "KING_CAPTURING_IT_SELF_ERROR"
  DEFAULT_MESSAGE = "A occupation cannot check itself."
  
class InvalidCheckEventException(CheckEventException, ValidationException):
  """"""
  ERROR_CODE = "INVALID_CHECK_EVENT_ERROR"
  DEFAULT_MESSAGE = "CheckEvent validator failed."
