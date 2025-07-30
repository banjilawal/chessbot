from typing import List

from chess.factory.board_populator import BoardPopulatorFactory
from chess.factory.human_player_builder import HumanPlayerBuilder
from chess.geometry.board import ChessBoard


from chess.factory.grid_builder import GridBuilder
from chess.geometry.board import ChessBoard
from chess.geometry.coordinate import Coordinate
from chess.piece.piece import ChessPiece
from chess.player.player_config import PlayerConfig


def get_rank_members(pieces: List[ChessPiece], rank: str):
    members = []
    for piece in pieces:
        if piece.rank.name.upper() == rank.upper():
            members.append(piece)
    return members


def main():
    # 1. Create players (with pieces inside them)
    white_player = HumanPlayerBuilder.build_player("White", player_config=PlayerConfig.WHITE)



    # 2. Create the grid and board
    grid = GridBuilder.build()
    board = ChessBoard(grid=grid)

    castles = get_rank_members(white_player.chess_pieces, "CASTLE")
    board.place_chess_piece_on_board(castles[0], Coordinate(row=0, column=0))
    board.place_chess_piece_on_board(castles[1], Coordinate(row=0, column=7))

    knights = get_rank_members(white_player.chess_pieces, "KNIGHT")
    board.place_chess_piece_on_board(knights[0], Coordinate(row=0, column=1))
    board.place_chess_piece_on_board(knights[1], Coordinate(row=0, column=6))

    bishops = get_rank_members(white_player.chess_pieces, "BISHOP")
    board.place_chess_piece_on_board(bishops[0], Coordinate(row=0, column=2))
    board.place_chess_piece_on_board(bishops[1], Coordinate(row=0, column=5))

    king = get_rank_members(white_player.chess_pieces, "KING")
    board.place_chess_piece_on_board(king[0], Coordinate(row=0, column=4))
    queen = get_rank_members(white_player.chess_pieces, "QUEEN")
    board.place_chess_piece_on_board(queen[0], Coordinate(row=0, column=3))

    pawns = get_rank_members(white_player.chess_pieces, "PAWN")
    for i in range(len(pawns)):
        board.place_chess_piece_on_board(pawns[i], Coordinate(row=1, column=i))

        # 1. Create players (with pieces inside them)
    black_player = HumanPlayerBuilder.build_player("Black", player_config=PlayerConfig.BLACK)

    # 2. Create the grid and board
    grid = GridBuilder.build()
    board = ChessBoard(grid=grid)

    castles = get_rank_members(white_player.chess_pieces, "CASTLE")
    board.place_chess_piece_on_board(castles[0], Coordinate(row=7, column=0))
    board.place_chess_piece_on_board(castles[1], Coordinate(row=7, column=7))

    knights = get_rank_members(white_player.chess_pieces, "KNIGHT")
    board.place_chess_piece_on_board(knights[0], Coordinate(row=7, column=1))
    board.place_chess_piece_on_board(knights[1], Coordinate(row=7, column=6))

    bishops = get_rank_members(white_player.chess_pieces, "BISHOP")
    board.place_chess_piece_on_board(bishops[0], Coordinate(row=7, column=2))
    board.place_chess_piece_on_board(bishops[1], Coordinate(row=7, column=5))

    king = get_rank_members(white_player.chess_pieces, "KING")
    board.place_chess_piece_on_board(king[0], Coordinate(row=7, column=4))
    queen = get_rank_members(white_player.chess_pieces, "QUEEN")
    board.place_chess_piece_on_board(queen[0], Coordinate(row=7, column=3))

    pawns = get_rank_members(white_player.chess_pieces, "PAWN")
    for i in range(len(pawns)):
        board.place_chess_piece_on_board(pawns[i], Coordinate(row=6, column=i))

    players = [white_player, black_player]






    # ✅ Now board is fully ready — can pass to GameDisplay or start game loop
    print("Board ready with pieces.")

    for player in players:
        for piece in player.chess_pieces:
            print(f"{piece.label} at {piece.current_coordinate()}")

if __name__ == "__main__":
    main()
