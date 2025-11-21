# src/chess/system/event/collision.py

"""
Module: chess.system.event.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException


__all__ = [
  'EventException'
]



class EventException(ChessException):
  """
  Super class of all exceptions `Event` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Event`
  exceptions.
  """
  ERROR_CODE = "EVENT_ERROR"
  DEFAULT_MESSAGE = "Event raised an rollback_exception."
