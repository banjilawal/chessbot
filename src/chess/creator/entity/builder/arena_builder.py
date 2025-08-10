from chess.arena.arena import Arena
from chess.board.board import ChessBoard
from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_board_builder import ChessBoardBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.owner_factory import OwnerFactory
from chess.creator.entity.factory.team_factory import TeamFactory
from chess.creator.team_placement_manager import TeamPlacementManager
from chess.owner.owner import Owner


class ArenaBuilder:

    @staticmethod
    def build() -> Arena:
        owners = OwnerFactory.assemble()

        arena = Arena(
            arena_id=id_emitter.arena_id,
            white_owner=owners[0],
            black_owner=owners[1],
            chess_board=ChessBoardBuilder.build(id_emitter.board_id)
         )
        TeamPlacementManager.place_teams(arena)
        return arena

def main():
    arena = ArenaBuilder.build()
    print(arena.chess_board)
    #
    # teams = TeamFactory.assemble()
    # white_team_owner = teams[0].owner
    # black_team_owner = teams[1].owner
    #
    #
    # arena = Arena(
    #     arena_id=id_emitter.arena_id
    # )
    # TeamPlacementManager.place_teams(arena)
    # return  arena
    #
    # print("white team owner", arena.white_owner,
    #       "\nwhite chess pieces:", len(arena.white_owner.team.chess_pieces))
    #
    # print("\nblack team owner", arena.black_owner,
    #       "\nblack chess pieces:", len(arena.black_owner.team.chess_pieces))


    #
    # for chess_piece in arena.white_owner.team.chess_pieces:
    #     print(chess_piece, " current coord", chess_piece.coordinate_stack.current_coordinate())

    # TeamPlacementManager.place_teams(arena)
    # print(arena.chess_board)

    # for square in arena.chess_board.occupied_squares():
    #     print(square, " occupied by", square.occupant.name)

    # for chess_piece in arena.white_owner.team.chess_pieces:
    #     print(chess_piece, " current coord", chess_piece.coordinate_stack.current_coordinate())
    # for square in arena.chess_board.squares:
    #     print(square)

if __name__ == "__main__":
    main()