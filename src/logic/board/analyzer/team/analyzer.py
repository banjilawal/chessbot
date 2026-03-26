# src/logic/board/analyzer/compute.py

"""
Module: logic.board.analyzer.analyzer
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.team import Team, TeamService
from logic.system import LoggingLevelRouter, RelationAnalysis, RelationReport
from logic.board import Board, BoardTeamAnalysisException, BoardValidationProcess


class BoardTeamRelationAnalysis(RelationAnalysis[Board, Team]):
    """
    Role:
        - Relation Analyzer
        - Report Generator

    Responsibilities:
        1.  Report the on the type of relationship is between the board and team.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Board,
                    candidate_satellite: Team,
                    board_validator: BoardValidationProcess = BoardValidationProcess(),
                    team_service: TeamService = TeamService(),
            ) -> RelationReport[Board, Team]

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate_primary: Board,
            candidate_satellite: Team,
            board_validator: BoardValidationProcess = BoardValidationProcess(),
            team_service: TeamService = TeamService(),
    ) -> RelationReport[Board, Team]:
        """
        Generate a report on the relationship between a board and team.
        
        Action:
            1.  Send an AnalyzerFailure exception if either candidate cannot be validated.
            2.  Otherwise, send the success result which can be:
                    -   No relation between them.
                    -   Board has expired link to team.
                    -   Team has not registered with board.
                    -   They have a fully bidirectional relation.
        Args::
            candidate_primary: Board
            candidate_satellite: Team
            board_validator: BoardValidationProcess
            team_service: TeamService
        Returns:
            RelationReport[Board, Team]
        Raises:
            BoardTeamAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the board is not secure.
        board_validation = board_validator.execute(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardTeamAnalysisException(
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Handle the case that, the team is unsecure.
        team_validation = team_service.validation.execute(candidate_satellite)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardTeamAnalysisException(
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        team = cast(Team, team_validation.payload)
        
        # Handle the case that, the team belongs to a different board.
        if board != team.board and not team in board.team_hash.table:
            return RelationReport.no_relation()
        
        if team in board.team_hash.table and team.board != board:
            return RelationReport.stale_link(primary=board)
        
        if not team in board.team_hash.table and team.board == board:
            return RelationReport.registration_missing(satellite=team)
        
        return RelationReport.bidirectional(primary=board, satellite=team)