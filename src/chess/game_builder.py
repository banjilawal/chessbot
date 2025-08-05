from typing import List

from chess.factory.old.board_populator import BoardPopulatorFactory
from chess.factory.grid_builder import GridBuilder

from chess.factory.old.expired_rank_factory import RankFactoryAntiPattern
from chess.factory.old.piece_factory import PieceFactory


from chess.geometry.board import ChessBoard
from chess.piece.piece import ChessPiece
from chess.player.player import Player
from chess.motion.abstract.motion_controller import MotionController


class GameBuilder:
    _board: ChessBoard
    _players: List[Player]
    _ranks: List[MotionController]
    _pieces: List[ChessPiece]

    def __init__(self, player_names: List[str]):
        self._ranks = []
        self._pieces = []
        self._players = []
        self._board = None

        self._build_game(player_names)

    def _build_game(self, player_names: List[str]):
        # Step 1: Build grid & board
        grid = GridBuilder.build()
        self._board = ChessBoard(grid=grid)

        # Step 2: Build ranks
        self._ranks = RankFactoryAntiPattern.run_factory()

        # Step 3: Build pieces for all ranks
        self._pieces = PieceFactory.run_factory(self._ranks)

        # Step 4: Assign pieces to players
        self._players = PlayerFactory.run_factory(player_names, self._pieces)

        # Step 5: Place pieces on the board
        BoardPopulatorFactory.populate(self._board, self._players)

    @property
    def board(self) -> ChessBoard:
        return self._board

    @property
    def players(self) -> List[Player]:
        return self._players

    @property
    def pieces(self) -> List[ChessPiece]:
        return self._pieces

    @property
    def ranks(self) -> List[MotionController]:
        return self._ranks


def main():
    builder = GameBuilder(player_names=["White", "Black"])

    board = builder.board
    players = builder.players

    print("🏁 Game ready!")
    print(board)

    for player in players:
        print(f"\n🧑‍🚀 Player: {player.name} ({player.color.name})")
        for piece in player.pieces:
            print(f" - {piece.label} at {piece.current_coordinate()}")

if __name__ == "__main__":
    main()