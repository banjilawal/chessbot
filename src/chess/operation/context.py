from typing import List

from chess.board import Board
from chess.team import Team

class ExecutionContext:
    """Container for execution dependencies"""

    def __init__(self, board: Board, teams: List[Team]): #, game_state: GameState = None):
        self.board = board
        self.teams = teams
        # self.game_state = game_state
        self.turn = None
        # ... other context fields

    def to_dict(self) -> dict:
        """Convert to dictionary for backward compatibility"""
        return {
            'board': self.board,
            'teams': self.teams,
            # 'game_state': self.game_state,
            'turn': self.turn
        }

#
# # Usage:
# context = ExecutionContext(board=current_board, teams=all_teams)
# outcome = executor.execute_directive(directive, context.to_dict())