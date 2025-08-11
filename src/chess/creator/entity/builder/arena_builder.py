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
        for p in arena.chess_board.occupied_squares():
            print(p, " occupied by", p.occupant.name)
        return arena

def main():
    arena = ArenaBuilder.build()
    print(arena.chess_board)
    for c in arena.white_owner.team.chess_pieces, arena.black_owner.team.chess_pieces:
        for p in c:
            print(p, " current coord", p.coordinate_stack.current_coordinate(), p.coordinate_stack.size())
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
    # for captor in arena.white_owner.team.chess_pieces:
    #     print(captor, " current coord", captor.coordinate_stack.current_coordinate())

    # TeamPlacementManager.place_teams(arena)
    # print(arena.chess_board)

    # for square in arena.chess_board.occupied_squares():
    #     print(square, " occupied by", square.occupant.name)

    # for captor in arena.white_owner.team.chess_pieces:
    #     print(captor, " current coord", captor.coordinate_stack.current_coordinate())
    # for square in arena.chess_board.squares:
    #     print(square)

if __name__ == "__main__":
    main()