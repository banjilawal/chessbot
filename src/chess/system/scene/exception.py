# src/chess/system/scene/exception.py

"""
Module: chess.system.scene.exception
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from chess.system import ChessException


class SceneException(ChessException):
  ERROR_CODE = "SCENE_ERROR"
  DEFAULT_MESSAGE = "A Scene object raised an exception"
