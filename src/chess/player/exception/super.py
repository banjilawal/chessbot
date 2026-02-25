# src/chess/player/exception.py

"""
Module: chess.player.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PLAYER EXCEPTION #======================#
    "PlayerException",
]

from chess.system import SuperClassException


# ======================# PLAYER EXCEPTION #======================#
class PlayerException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of PlayerDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "PLAYER_ERROR"
    MSG = "Player raised an exception."