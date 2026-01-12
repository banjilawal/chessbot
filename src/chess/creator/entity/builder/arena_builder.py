from chess.arena.arena import Arena
from chess.system.identity.id import id_emitter
from chess.board.builder import ChessBoardBuilder
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
      print(p, " current point", p.positions.current_coord(), p.positions.size())
  #
  # team_service = TeamFactory.assemble()
  # white_team_owner = team_service[0].owner
  # black_team_owner = team_service[1].owner
  #
  #
  # arena = Arena(
  #   arena_id=id_emitter.arena_id
  # )
  # TeamPlacementManager.place_teams(arena)
  # return arena
  #
  # print("white team_name owner", arena.white_owner,
  #    "\nwhite chess pieces:", len(arena.white_owner.team_name.chess_pieces))
  #
  # print("\nblack team_name owner", arena.black_owner,
  #    "\nblack chess pieces:", len(arena.black_owner.team_name.chess_pieces))


  #
  # for captor in arena.white_owner.team_name.chess_pieces:
  #   print(captor, " current point", captor.coordinate_stack.current_coordinate())

  # TeamPlacementManager.place_teams(arena)
  # print(arena.chess_board)

  # for square_name in arena.chess_board.occupied_squares():
  #   print(square_name, " occupied by", square_name.occupant.visitor_name)

  # for captor in arena.white_owner.team_name.chess_pieces:
  #   print(captor, " current point", captor.coordinate_stack.current_coordinate())
  # for square_name in arena.chess_board.squares:
  #   print(square_name)

if __name__ == "__main__":
  main()