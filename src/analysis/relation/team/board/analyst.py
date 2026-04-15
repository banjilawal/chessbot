# src/analysis/relation/team/board/analyst.py

"""
Module: analysis.relation.team.board.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analysis import RelationAnalyst
from analysis.relation.team.board.exception import BoardTeamAnalysisException
from integrity import BoardService
from microservice import TeamService
from model import Board, Team
from report import RelationReport
from result import AnalysisResult
from result.category import ResultCategory
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
            board_validator: BoardService | None = None,
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
            BoardTeamAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        if board_validator is None:
            board_validator = BoardService()
        
        if team_service is None:
            team_service = TeamService()
        
        # Handle the case that, the board is not certified as safe.
        board_validation_result = board_validator.validate(candidate_primary)
        if board_validation_result.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    rslt_type=ResultCategory.ANALYSIS_RESULT,
                    ex=board_validation_result.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation_result.payload)
        
        # Handle the case that, the team_binder has a board inconsistency.
        if board.team_binder.board != board:
            if board_validation_result.is_failure:
                # Return the exception chain on failure.
                return AnalysisResult.failure(
                    BoardTeamAnalysisException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BoardTeamAnalysisException.MSG,
                        err_code=BoardTeamAnalysisException.ERR_CODE,
                        rslt_type=ResultCategory.ANALYSIS_RESULT,
                        ex=board_validation_result.exception,
                    )
                )
        # Handle the case that, the team is not certified as safe.
        team_validation_result = team_service.validator.validate(candidate_satellite)
        if team_validation_result.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    rslt_type=ResultCategory.ANALYSIS_RESULT,
                    ex=team_validation_result.exception,
                )
            )
        team = cast(Team, team_validation_result.payload)
        
        # Handle the case that, the team belongs to a different board.
        if board != team.board:
            return AnalysisResult.success(RelationReport.no_relation())
        
        # Handle the case that, the team has not registered with the board.
        if team.schema not in board.team_binder.schemas:
            return AnalysisResult.success(RelationReport.registration_missing(team))
        
        # Handle the case that, the board has a stale link to the team.
        if team in board.team_binder.teams and team.board != board:
            return AnalysisResult.success(RelationReport.stale_link(board))
        
        # Last case is the
        return AnalysisResult.success(RelationReport.bidirectional(primary=board, satellite=team))