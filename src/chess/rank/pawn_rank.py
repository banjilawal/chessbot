from typing import List

from chess.board.board import Board
from chess.config.rank import RankProfile
from chess.creator.emit import id_emitter
from chess.exception.rank_exception import PawnRankException
from chess.exception.walk import PawnWalkException
from chess.flow.occupy import OccupationFlow
from chess.geometry.coord import Coord
from chess.geometry.path import Path, Line
from chess.geometry.quadrant import Quadrant
from chess.rank.queen_rank import PromotedQueen
from chess.system.send import OccupationRequest
from chess.piece.piece import Piece


class Pawn(PromotedQueen):

    def __init__(
        self,
        name:str=RankProfile.PAWN.name,
        letter:str=RankProfile.PAWN.letter,
        value:int=RankProfile.PAWN.value,
        per_side:int=RankProfile.PAWN.per_side,
        quadrants:[Quadrant]=RankProfile.PAWN.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Pawn.walk"

        try:
            if not (
                self._is_opening(piece, destination) or
                self._is_advance(piece, destination) or
                self._is_attack(piece, destination)
            ):
                raise PawnWalkException(f"{method}: {PawnWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except PawnWalkException as e:
            raise PawnRankException(f"{method}: {PawnRankException.DEFAULT_MESSAGE}") from e


    @staticmethod
    def _is_opening(piece: Piece, destination: Coord):
        return piece.positions.size() == 1 and Path(piece.current_position, destination).line == Line.PAWN_OPENING


    @staticmethod
    def _is_advance(self, piece: Piece, destination: Coord):
        return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ADVANCE

    @staticmethod
    def _is_attack(self, piece: Piece, destination: Coord):
        return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ATTACK

