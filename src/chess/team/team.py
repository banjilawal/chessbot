from dataclasses import field
from typing import Dict, Optional

from chess.common.config import ChessPieceConfig
from chess.figure.chess_piece import ChessPiece
from chess.team.home import TeamHome
from podscape.constants import GameColor

class Team:
    team_id: int
    color: GameColor
    home: TeamHome
    piece_registry: Dict[ChessPieceConfig, Dict[int, Optional[ChessPiece]]] = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'home_row', 6 if self.color == GameColor.RED else 1)
        object.__setattr__(self, 'goal_row', 0 if self.color == GameColor.RED else 7)
        object.__setattr__(self, 'advancement_direction', -1 if self.color == GameColor.RED else +1)

        initial_pieces = self._generate_initial_registry()
        object.__setattr__(self, 'piece_registry', initial_pieces)

    def _generate_initial_registry(self) -> Dict[str, Optional[ChessPiece]]:
        ranks = {
            "pawn": 8,
            "rook": 2,
            "knight": 2,
            "bishop": 2,
            "queen": 1,
            "king": 1,
        }
        registry = {}
        for rank_name, count in ranks.items():
            for i in range(1, count + 1):
                piece_id = f"{rank_name}_{i}" if count > 1 else rank_name
                registry[piece_id] = ChessPiece(team=self, rank_name=rank_name, chess_piece_id=piece_id)
        return registry