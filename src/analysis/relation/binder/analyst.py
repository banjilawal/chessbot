# src/analysis/relation/binder/analyst.py

"""
Module: analysis.relation.binder.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analysis import RelationAnalyst
from err import BoardBinderAnalysisAnalysisException
from integrity import BoardValidator
from microservice import BoardService
from model import Board, BoardBinder
from operation import BoardTeamBinderValidator
from report import RelationReport
from result import AnalysisResult, MethodResultType
from system import LoggingLevelRouter


class BoardTeamBinderRelationAnalyst(RelationAnalyst[Board, BoardBinder]):
    """
    Role:
        - Relation Analyst
        - Report Generator

    Responsibilities:
        1.  Report the on the type of relationship is between the board and binder.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Board,
                    candidate_satellite: Binder,
                    board_validator: BoardValidator = BoardValidator(),
                    team_binder_validator: TeamBinderValidator = TeamBinderValidator(),
            ) -> RelationReport[Board, Binder]

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Board,
            candidate_satellite: BoardBinder,
            board_validator: BoardValidator | None = None,
            team_binder_validator: BoardTeamBinderValidator | None = None,
    ) -> AnalysisResult[RelationReport[Board, BoardBinder]]:
        """
        Generate a report on the relationship between a board and binder.
        
        Action:
            1.  Send an AnalyzerFailure exception if either rank cannot be validated.
            2.  Otherwise, send the success result which can be:
                    -   No relation between them.
                    -   Board has expired link to binder.
                    -   Binder has not registered with board.
                    -   They have a fully bidirectional relation.
        Args::
            candidate_primary: Board
            candidate_satellite: Binder
            board_validator: BoardValidator
            team_binder_validator: TeamBinderValidator
        Returns:
            RelationReport[Board, Binder]
        Raises:
            BoardBinderAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        if board_validator is None:
            board_validator = BoardService()
        
        if team_binder_validator is None:
            team_binder_validator = BoardTeamBinderValidator()
        
        # Handle the case that, the board is not certified as safe.
        board_validation_result = board_validator.validate(candidate_primary)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                BoardBinderAnalysisAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardBinderAnalysisAnalysisException.MSG,
                    err_code=BoardBinderAnalysisAnalysisException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation_result.payload)
        
        # Handle the case that, the binder is not certified as safe.
        team_binder_validation_result = team_binder_validator.validate(candidate_satellite)
        if team_binder_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                BoardBinderAnalysisAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardBinderAnalysisAnalysisException.MSG,
                    err_code=BoardBinderAnalysisAnalysisException.ERR_CODE,
                    ex=team_binder_validation_result.exception,
                )
            )
        team_binder = cast(BoardBinder, team_binder_validation_result.payload)
        
        # Handle the case that, the binder belongs to a different board.
        if board.team_binder != team_binder and team_binder.primary != board :
            return AnalysisResult.success(RelationReport.no_relation())
        
        # Handle the case that, the board has a stale link to team_binder.
        if board.team_binder == team_binder and team_binder.primary != board:
            return AnalysisResult.success(
                RelationReport.stale_link(
                    primary=board
                )
            )
        # Handle the case that, the binder has not registered with its board.
        if board.team_binder != team_binder and team_binder.primary == board:
            return AnalysisResult.success(
                RelationReport.registration_missing(
                    satellite=team_binder
                )
            )
        # Otherwise, there is a bidirectional relationship between the binder and the board.
        return AnalysisResult.success(
            RelationReport.bidirectional(
                primary=board,
                satellite=team_binder
            )
        )