from chess.arena.arena import Arena
from chess.board.board import ChessBoard
from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.service.chess_board_builder import ChessBoardBuilder
from chess.owner.owner import Owner


class ArenaBuilder:

    @staticmethod
    def build(
        arena_id:int,
        white_team_owner: Owner,
        black_team_owner: Owner,
        chess_board: ChessBoard
    ) -> Arena:
        if white_team_owner.team_stack.is_empty():
            white_team = TeamBuilder.build(white_team_owner, TeamConfig.WHITE)
        if black_team_owner.team_stack.is_empty():
            black_team = TeamBuilder.build(black_team_owner, TeamConfig.BLACK)

        return Arena(
            arena_id=arena_id,
            white_owner=white_team_owner,
            black_owner=black_team_owner,
            chess_board=chess_board
         )

def main():
    white_team = TeamBuilder.build(OwnerBuilder.build(id_emitter.owner_id), TeamConfig.WHITE)
    black_team = TeamBuilder.build(OwnerBuilder.build(id_emitter.owner_id), TeamConfig.BLACK)
    chess_board = ChessBoardBuilder.build()

    arena = ArenaBuilder.build(id_emitter.arena_id, white_team.owner, black_team.owner, chess_board)

    print(arena.white_owner, arena.black_owner)
    print(
        arena.white_owner.team_stack.size(),
        arena.black_owner.team_stack.size()
    )


if __name__ == "__main__":
    main()