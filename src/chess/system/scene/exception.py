# src/chess/system/scene/collision.py

"""
Module: chess.system.scene.exception
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from chess.system import ChessException


class SceneException(ChessException):
  ERR_CODE = "SCENE_EXCEPTION"
  MSG = "A Scene object raised an exception"
