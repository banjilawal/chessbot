# src/chess/game/result/stack.py

"""
Module: chess.game.result.stack
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.game.result import GameResult
from chess.system import ResultStack


class GameResultStack(ResultStack[GameResult]):
    def __init__(self):
        super().__init__()