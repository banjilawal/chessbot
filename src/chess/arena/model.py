from chess.board.board import Board
from chess.competitor.model import CyberneticCompetitor
from chess.competitor.model import Competitor
from chess.side.move import Move


class Arena:
    _id: int
    _white_owner: Competitor
    _black_owner: Competitor
    _chess_board: Board

    def __init__(self, arena_id: int, white_owner: Competitor, black_owner: Competitor, chess_board: Board):
        self._id = arena_id
        self._white_owner = white_owner
        self._black_owner = black_owner
        self._chess_board = chess_board

    @property
    def id(self) -> int:
        return self._id


    @property
    def white_owner(self) -> Competitor:
        return self._white_owner


    @property
    def black_owner(self) -> Competitor:
        return self._black_owner


    @property
    def chess_board(self) -> Board:
        return self._chess_board


    def execute_move(self, move: Move):
        self._board.capture_square(move.team_member, move.destination)


    def survey_board(self, cybernaut: CyberneticCompetitor):
        cybernaut.engine._scout_master.send_scouts(cybernaut, self._chess_board)





