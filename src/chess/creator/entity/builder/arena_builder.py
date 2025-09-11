from chess.arena.model import Arena
from chess.common.emit import id_emitter
from chess.creator.entity.builder.chess_board_builder import ChessBoardBuilder
from chess.creator.entity.factory.owner_factory import OwnerFactory
from chess.creator.team_placement_manager import TeamPlacementManager


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
    for c in arena.white_owner.team.roster, arena.black_owner.team.roster:
        for p in c:
            print(p, " current coord", p.positions.current_coord(), p.positions.size())
    #
    # teams = TeamFactory.assemble()
    # white_team_owner = teams[0].commander
    # black_team_owner = teams[1].commander
    #
    #
    # arena = Arena(
    #     arena_id=id_emitter.arena_id
    # )
    # TeamPlacementManager.place_teams(arena)
    # return  arena
    #
    # print("white team commander", arena.white_owner,
    #       "\nwhite chess pieces:", len(arena.white_owner.team.chess_pieces))
    #
    # print("\nblack team commander", arena.black_owner,
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