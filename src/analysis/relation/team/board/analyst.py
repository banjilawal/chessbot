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
from err import BoardTeamAnalysisException
from model import Board, Team
from report import RelationReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter
from validation import BoardValidator, TeamValidator


class BoardTeamRelationAnalyst(RelationAnalyst[Board, Team]):
    """
    Role:
        - Relation Analyst
        - Report Generator

    Responsibilities:
        1.  Analyze the relationship between Team and Board instances.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Board,
                    candidate_satellite: Team,
                    board_validator: BoardValidator = BoardValidator(),
                    team_validator: TeamValidator = TeamValidator(),
            ) -> RelationReport[Board, Team]

    Super:
        Analyst
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Board,
            candidate_satellite: Team,
            board_validator: BoardValidator | None = None,
            team_validator: TeamValidator | None = None,
    ) -> AnalysisResult[RelationReport]:
        """
        Generate a report on the relationship between a board and team.
        
        Action:
            1.  Send an exception chain in the AnalysisResult if either candidate is flagged by
                a validator.
            2.  Otherwise, test that
                    -   The board contains the team.
                    -   The team belongs to the board.
            3.  Then, send the test results in the success result.
        Args:
            candidate_primary: Board
            candidate_satellite: Team
            board_validator: BoardValidator
            team_validator: TeamValidator
        Returns:
            AnalysisResult[RelationReport]
        Raises:
            BoardTeamAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        if board_validator is None:
            board_validator = BoardValidator()
        if team_validator is None:
            team_validator = TeamValidator()
        
        # Handle the case that, the board is not certified as safe.
        board_validation_result = board_validator.validate(candidate_primary)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=board_validation_result.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation_result.payload)
        
        # Handle the case that, the team_binder has a board inconsistency.
        if board.binder_controller.binder != board:
            if board_validation_result.is_failure:
                # Send the exception chain on failure.
                return AnalysisResult.failure(
                    BoardTeamAnalysisException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BoardTeamAnalysisException.MSG,
                        err_code=BoardTeamAnalysisException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=board_validation_result.exception,
                    )
                )
        # Handle the case that, the team is not certified as safe.
        team_validation_result = team_validator.validator.validate(candidate_satellite)
        if team_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                BoardTeamAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamAnalysisException.MSG,
                    err_code=BoardTeamAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=team_validation_result.exception,
                )
            )
        team = cast(Team, team_validation_result.payload)
        
        if team.board != board and board.binder_controller.binder.satellite_table[team.schema] != team:
            return AnalysisResult.success(RelationReport.no_relation())
        
        # Handle the case that, the team has not registered with the board.
        if team.schema not in board.binder_controller.binder.schema_list:
            return AnalysisResult.success(RelationReport.registration_missing(team))
        
        # Handle the case that, the board has a stale link to the team.
        if team in board.binder_controller.binder.satellite_list and team.board != board:
            return AnalysisResult.success(RelationReport.stale_link(board))
        
        # Last case is the
        return AnalysisResult.success(RelationReport.bidirectional(primary=board, satellite=team))