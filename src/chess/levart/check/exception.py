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
  ERR_CODE = "CHECK_EXCEPTION"
  MSG = "A check event raised an exception."


#======================# ATTACK_EVENT VALIDATION EXCEPTION #======================#
class NullCheckEventException(CheckEventException, NullException):
  """"""
  ERR_CODE = "NULL_CHECK_EVENT_EXCEPTION"
  MSG = "CheckEvent cannot be null."

class KingCheckingItselfException(CheckEventException):
  """"""
  ERR_CODE = "KING_CAPTURING_IT_SELF_EXCEPTION"
  MSG = "A occupation cannot check itself."
  
class InvalidCheckEventException(CheckEventException, ValidationException):
  """"""
  ERR_CODE = "INVALID_CHECK_EVENT_EXCEPTION"
  MSG = "CheckEvent validation failed."
