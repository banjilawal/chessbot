from typing import List
from chess.geometry.coordinate import Coordinate
from chess.geometry.board import ChessBoard
from chess.player.player import Player
from chess.piece.piece import ChessPiece


class BoardPopulatorFactory:

    @staticmethod
    def populate(board: ChessBoard, players: List[Player]) -> None:
        for player in players:
            is_white = player.color.name.upper() == "IVORY"
            back_row = 0 if is_white else 7
            pawn_row = 1 if is_white else 6

            # Group pieces by rank acronym: "P", "K", "Q", etc.
            grouped: dict[str, List[ChessPiece]] = {}
            for piece in player.pieces:
                acronym = piece.rank.acronym
                grouped.setdefault(acronym, []).append(piece)

            # Back rank layout in chess order
            layout = ["C", "N", "B", "Q", "K", "B", "N", "C"]

            # Place major pieces
            for col, code in enumerate(layout):
                if code not in grouped or not grouped[code]:
                    print(f"⚠️  Missing piece {code} for player {player.name}")
                    continue
                piece = grouped[code].pop(0)
                coord = Coordinate(row=back_row, column=col)
                result = board.place_chess_piece_on_board(piece, coord)
                if result.is_failure:
                    print(f"❌ Failed to place {piece.label} at {coord}: {result.message}")

            # Place pawns
            for col in range(8):
                if "P" not in grouped or not grouped["P"]:
                    print(f"⚠️ Not enough pawns for player {player.name}")
                    break
                pawn = grouped["P"].pop(0)
                coord = Coordinate(row=pawn_row, column=col)
                result = board.place_chess_piece_on_board(pawn, coord)
                if result.is_failure:
                    print(f"❌ Failed to place {pawn.label} at {coord}: {result.message}")
