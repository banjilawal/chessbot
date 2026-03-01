# src/logic/system/event/collision.py

"""
Module: logic.system.event.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.system import ChessException


__all__ = [
  'EventException'
]



class EventException(ChessException):
  """
  Super class of all exception `Event` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Event`
  exception.
  """
  ERR_CODE = "EVENT_EXCEPTION"
  MSG = "Event raised an exception."
