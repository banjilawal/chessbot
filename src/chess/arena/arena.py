# src/chess/arena/arena.py

"""
Module: chess.arena.arena
Author: Banji Lawal
Created: 2025-08-05
version: 1.0.0
"""
from typing import List

from chess.piece import PieceContext
from chess.system import BuildResult, id_emitter
from chess.team import Team, UniqueTeamDataService
from chess.agent import Agent
from chess.board import BoardService

class Arena:
    _id: int
    _white_team: Team
    _black_team: Team
    _teams: List[Team]
    _board: BoardService
    
    def __init__(self, id: int, teams: List[Team], board: BoardService):
        self._id = id
        self._board = board
        self._teams = teams
        self._white_team = self.teams[0]
        self._black_team = self.teams[1]

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def board(self) -> BoardService:
        return self._board
    
    @property
    def white_team(self) -> Team:
        return self._teams[0]
    
    @property
    def black_team(self) -> Team:
        return self._teams[1]
    
    @property
    def teams(self) -> List[Team]:
        return self._teams
    
    @property
    def agents(self) -> List[Agent]:
        return [self._white_team.agent, self._black_team.agent]
    
    @property
    def captured_pieces(self) -> List[Piece]:
        return [self._white_team.hostages, self._black_team.hostages]
    
    def populate_teams(self):
        for team in self.teams:
            self._fill_team_roster(team)
    
    def _fill_team_roster(self, team: Team) -> BuildResult[List[Piece]]:
        pieces = []
        for order in team.schema.battle_order:
            build_result = team.roster.piece_service.builder.build(
                team=team,
                name=order.name,
                rank=order.rank,
                id=id_emitter.piece_id,
                opening_square_name=order.opening_square_name,
            )
            if build_result.is_failure:
                return BuildResult.failure(build_result.exception)
            search_result = team.roster.search(context=PieceContext(id=build_result.payload.id))
            if search_result.is_failure:
                return BuildResult.failure(search_result.exception)
            if search_result.is_empty:
                insertion_result = team.roster.push_unique_item(build_result.payload.id)
                if insertion_result.is_failure:
                    return BuildResult.failure(insertion_result.exception)
            pieces.append(build_result.payload)
            return BuildResult.success(pieces)
                
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Arena):
            return self.id == other.id
        return False
    
