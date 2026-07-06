# src/analyzer/relation/token/team/analyst.py

"""
Module: analyzer.relation.token.team.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import RelationAnalyzer
from err import TeamTokenRelationAnalysisException
from model import Team, Token, TokenContext
from report import RelationReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter
from validator import TeamValidator, TokenValidator


class TeamTokenRelationAnalyzer(RelationAnalyzer[Team, Token]):
    """
    Role:
        - Relation Analyst
        - Report Generator

    Responsibilities:
        1.  Analyze the relationship between Token and Team instances.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Team,
                    candidate_satellite: Token,
                    team_validator: TeamValidator = TeamValidator(),
                    token_validator: TokenValidator = TokenValidator(),
            ) -> RelationReport[Team, Token]

    Super:
        Analyst
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Team,
            candidate_satellite: Token,
            team_validator: TeamValidator | None = None,
            token_validator: TokenValidator | None = None,
    ) -> AnalysisResult[RelationReport]:
        """
        Generate a report on the relationship between a team and token.
        
        Action:
            1.  Send an exception chain in the AnalysisResult if either candidate is flagged by
                a validator.
            2.  Otherwise, test that
                    -   The team contains the token.
                    -   The token belongs to the team.
            3.  Then, send the test results in the success result.
        Args:
            candidate_primary: Team
            candidate_satellite: Token
            team_validator: TeamValidator
            token_validator: TokenValidator
        Returns:
            AnalysisResult[RelationReport]
        Raises:
            TeamTokenRelationAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if team_validator is None:
            team_validator = TeamValidator()
        if token_validator is None:
            token_validator = TokenValidator()
        
        # Handle the case that, the team is not certified as safe.
        team_validation_result = team_validator.validate(candidate_primary)
        if team_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                TeamTokenRelationAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamTokenRelationAnalysisException.MSG,
                    err_code=TeamTokenRelationAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=team_validation_result.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        team = cast(Team, team_validation_result.payload)
        
        # Handle the case that, the token is not certified as safe.
        token_validation_result = token_validator.execute(candidate_satellite)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                TeamTokenRelationAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamTokenRelationAnalysisException.MSG,
                    err_code=TeamTokenRelationAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_validation_result.exception,
                )
            )
        token = cast(Token, token_validation_result.payload)
        
        if team.roster.is_empty and token.team == team:
            return AnalysisResult.success(RelationReport.bidirectional(primary=team, satellite=token))
        
        token_search_result = team.roster.search(context=TokenContext(id=token.id))
        if token_search_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                TeamTokenRelationAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamTokenRelationAnalysisException.MSG,
                    err_code=TeamTokenRelationAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_search_result.exception,
                )
            )
        if token.team != team and token_search_result.is_empty:
            return AnalysisResult.success(RelationReport.no_relation())
        
        if token.team == team and token_search_result.is_empty:
            return AnalysisResult.success(RelationReport.registration_missing(satellite=token))
        
        if token.team != team and token_search_result.is_success:
            return AnalysisResult.success(RelationReport.stale_link(primary=team))
        
        return AnalysisResult.success(RelationReport.bidirectional(primary=team, satellite=token))