from typing import List

from chess.board.element.square import Square
from chess.token.obstruction import Obstruction
from chess.token.piece import ChessPiece


class ScoutReportAnalysis:
    _id: int
    _chess_piece: ChessPiece
    _enemies: List[ChessPiece]
    _vacant_squares: List[Square]
    _obstructions: List[Obstruction]

    def __init__(self,
         neighbor_table_id: int,
         chess_piece: ChessPiece,
         enemies: List[ChessPiece],
         vacant_squares: List[Square],
         obstructions: List[Obstruction]
     ):
        self._id = neighbor_table_id
        self._chess_piece = chess_piece
        self._enemies = enemies
        self._vacant_squares = vacant_squares
        self._obstructions = obstructions

    @property
    def id(self) -> int:
        return self._id

    @property
    def chess_piece(self) -> ChessPiece:
        return self._chess_piece

    @property
    def enemies(self) -> List[ChessPiece]:
        return self._enemies

    @property
    def vacant_squares(self) -> List[Square]:
        return self._vacant_squares

