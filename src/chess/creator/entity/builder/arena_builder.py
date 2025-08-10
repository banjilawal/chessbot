from chess.arena.arena import Arena
from chess.board.board import ChessBoard
from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_board_builder import ChessBoardBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.team_factory import TeamFactory
from chess.creator.team_placement_manager import TeamPlacementManager
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

    teams = TeamFactory.assemble()
    white_team_owner = teams[0].owner
    black_team_owner = teams[1].owner


    arena = ArenaBuilder.build(
        id_emitter.arena_id,
        white_team_owner,
        black_team_owner,
        ChessBoardBuilder.build(id_emitter.board_id)
    )

    print("white team owner", arena.white_owner,
          "\nwhite chess pieces:", len(arena.white_owner.team.chess_pieces))

    print("\nblack team owner", arena.black_owner,
          "\nblack chess pieces:", len(arena.black_owner.team.chess_pieces))


    #
    # for chess_piece in arena.white_owner.team.chess_pieces:
    #     print(chess_piece, " current coord", chess_piece.coordinate_stack.current_coordinate())

    TeamPlacementManager.place_teams(arena)
    print(arena.chess_board)
    # for chess_piece in arena.white_owner.team.chess_pieces:
    #     print(chess_piece, " current coord", chess_piece.coordinate_stack.current_coordinate())
    # for square in arena.chess_board.squares:
    #     print(square)

if __name__ == "__main__":
    main()