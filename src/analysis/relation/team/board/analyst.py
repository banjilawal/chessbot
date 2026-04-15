# src/analysis/relation/team/board/analyst.py

"""
Module: analysis.relation.team.board.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analysis import RelationAnalyst
from analysis.relation.team.board.exception import BoardTeamAnalystException
from integrity import BoardValidator
from microservice import TeamService
from model import Board, Team
from report import RelationReport
from result import AnalysisResult
from system import LoggingLevelRouter


class BoardTeamRelationAnalyst(RelationAnalyst[Board, Team]):
    """
    Role:
        - Relation Analyst
        - Report Generator

    Responsibilities:
        1.  Report the on the type of relationship is between the board and team.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Board,
                    candidate_satellite: Team,
                    board_validator: BoardValidator = BoardValidator(),
                    team_service: TeamService = TeamService(),
            ) -> RelationReport[Board, Team]

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Board,
            candidate_satellite: Team,
            board_validator: BoardValidator | None = None,
            team_service: TeamService | None = None,
    ) -> AnalysisResult[RelationReport[Board, Team]]:
        """
        Generate a report on the relationship between a board and team.
        
        Action:
            1.  Send an AnalyzerFailure exception if either rank cannot be validated.
            2.  Otherwise, send the success result which can be:
                    -   No relation between them.
                    -   Board has expired link to team.
                    -   Team has not registered with board.
                    -   They have a fully bidirectional relation.
        Args::
            candidate_primary: Board
            candidate_satellite: Team
            board_validator: BoardValidator
            team_service: TeamService
        Returns:
            RelationReport[Board, Team]
        Raises:
            BoardTeamAnalystException
        """
        method = f"{cls.__name__}.analyze"
        
        if board_validator is None:
            board_validator = BoardValidator()
        
        if team_service is None:
            team_service = TeamService()
        
        # Handle the case that, the board is not secure.
        board_validation = board_validator.validate(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalystException(
                    msg=BoardTeamAnalystException.MSG,
                    err_code=BoardTeamAnalystException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Handle the case that, the team is unsecure.
        team_validation = team_service.validator.validate(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalystException(
                    msg=BoardTeamAnalystException.MSG,
                    err_code=BoardTeamAnalystException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        # Handle the case that, the team belongs to a different board.
        if board != team.board and not team in board.team_hash.table:
            return RelationReport.no_relation()
        
        if
        
        if team in board.team_hash.table and team.board != board:
            return RelationReport.stale_link(primary=board)
        
        if not team in board.team_hash.table and team.board == board:
            return RelationReport.registration_missing(satellite=team)
        
        return RelationReport.bidirectional(primary=board, satellite=team)