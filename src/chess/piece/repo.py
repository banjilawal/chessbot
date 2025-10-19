from typing import List, Optional

from chess.piece.model.piece import Piece


class ChessPieceRepo:
  _chess_pieces: List[Piece]


  def __init__(self,):
    self._chess_pieces = []

  def __len__(self):
    return len(self._chess_pieces)


  def add(self, chess_piece: Piece):
    if chess_piece not in self._chess_pieces and chess_piece is not None:
      self._chess_pieces.append(chess_piece)


  def chess_piece_by_id(self, chess_piece_id: int) -> Optional[Piece]:
    for chess_piece in self._chess_pieces:
      if chess_piece.id == chess_piece_id:
        return chess_piece
    return None


  def filter_by_team(self, owner_id: int) -> List[Piece]:
    matches: List[Piece] = []

    for chess_piece in self._chess_pieces:
      if chess_piece.team.commander.id == owner_id and chess_piece not in matches:
        matches.append(chess_piece)
    return matches

