from chess.board.board import ChessBoard
from chess.board.map_service import MapService
from chess.owner.model.cybernetic_owner import CyberneticOwner
from chess.owner.model.owner import Owner
from chess.team.move import Move
from chess.team.team_service import TeamService


class Arena:
    _id: int
    _white_owner: Owner
    _black_owner: Owner
    _chess_board: ChessBoard

    def __init__(self, arena_id: int, white_owner: Owner, black_owner: Owner, chess_board: ChessBoard):
        self._id = arena_id
        self._white_owner = white_owner
        self._black_owner = black_owner
        self._chess_board = chess_board

    @property
    def id(self) -> int:
        return self._id


    @property
    def white_owner(self) -> Owner:
        return self._white_owner


    @property
    def black_owner(self) -> Owner:
        return self._black_owner


    @property
    def chess_board(self) -> ChessBoard:
        return self._chess_board


    def execute_move(self, move: Move):
        self._board.capture_square(move.team_member, move.destination)


    def survey_board(self, cybernaut: CyberneticOwner):
        cybernaut.engine._scout_master.send_scouts(cybernaut, self._chess_board)





