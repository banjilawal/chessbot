from typing import List, Optional, TYPE_CHECKING

from chess.common.game_color import GameColor
from chess.team.model.piece import ChessPiece
from chess.team.model.team import Team

# if TYPE_CHECKING:
#     from chess.team.model.team import Team


class TeamService:
    _teams: List[Team]

    def __init__(self, teams: List[Team]):
        self._teams = teams

    @property
    def teams(self) -> List[Team]:
        return self._teams


    def chess_pieces(self) -> List[ChessPiece]:
        pieces = []
        for team in self._teams:
            pieces.extend(team.chess_pieces)
        return pieces


    def size(self) -> int:
        return len(self._teams)


    def find_team_by_id(self, team_id: int) -> Optional[Team]:
        for team in self._teams:
            if team.id == team_id:
                return team
        return None


    def find_team_by_color(self, color: GameColor) -> Optional[Team]:
        for team in self._teams:
            if team.color == color:
                return team
        return None


    def find_team_by_letter(self, letter: str) -> Optional[Team]:
        for team in self._teams:
            if team.letter == letter:
                return team
        return None


    def find_chess_piece_by_id(self, chess_piece_id: int) -> Optional[ChessPiece]:
        for team in self._teams:
            for chess_piece in team.chess_pieces:
                if chess_piece.id == chess_piece_id:
                    return chess_piece
        return None


    def find_chess_piece_by_name(self, name: str) -> Optional[ChessPiece]:
        for team in self._teams:
            for chess_piece in team.chess_pieces:
                if chess_piece.name == name:
                    return chess_piece
        return None