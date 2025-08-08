from typing import List, Optional

from chess.team.element.piece import ChessPiece


class ChessPieceRepo:
    _chess_pieces: List[ChessPiece]

    def __init__(self,):
        self._chess_pieces = []

    def add(self, chess_piece: ChessPiece):
        if chess_piece not in self._chess_pieces and chess_piece is not None:
            self._chess_pieces.append(chess_piece)

    def find(self, chess_piece_id: int) -> Optional[ChessPiece]:
        for chess_piece in self._chess_pieces:
            if chess_piece.id == chess_piece_id:
                return chess_piece
        return None

    def filter_by_owner_id(self, owner_id: int) -> List[ChessPiece]:
        matches: List[ChessPiece] = []

        for chess_piece in self._chess_pieces:
            if chess_piece.team.owner.id == owner_id and chess_piece not in matches:
                matches.append(chess_piece)
        return matches

