# src/analysis/relation/token/square/analyzer.py

"""
Module: analysis.relation.token.square.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analysis import RelationAnalyzer
from model import Square, Token
from report import RelationReport
from util import LoggingLevelRouter
from result import AnalysisResult, MethodResultType
from err import SquareTokenRelationAnalysisException
from validation import SquareValidator, TokenValidator


class SquareTokenRelationAnalyzer(RelationAnalyzer[Square, Token]):
    """
    Role:
        - Relation Analyzer
        - Report Generator

    Responsibilities:
        1.  Analyze the relationship between Token and Square instances.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Square,
                    candidate_satellite: Token,
                    square_validator: SquareValidator = SquareValidator(),
                    token_validator: TokenValidator = TokenValidator(),
            ) -> RelationReport[Square, Token]

    Super:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Square,
            candidate_satellite: Token,
            square_validator: SquareValidator | None = None,
            token_validator: TokenValidator | None = None,
    ) -> AnalysisResult[RelationReport]:
        """
        Generate a report on the relationship between a square and token.
        
        Action:
            1.  Send an exception chain in the AnalysisResult if either candidate is flagged by
                a validator.
            2.  Otherwise, test that
                    -   The square contains the token.
                    -   The token belongs to the square.
            3.  Then, send the test results in the success result.
        Args:
            candidate_primary: Square
            candidate_satellite: Token
            square_validator: SquareValidator
            token_validator: TokenValidator
        Returns:
            AnalysisResult[RelationReport]
        Raises:
            SquareTokenRelationAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if square_validator is None:
            square_validator = SquareValidator()
        if token_validator is None:
            token_validator = TokenValidator()
        
        # Handle the case that, the square is not certified as safe.
        square_validation_result = square_validator.validate(candidate_primary)
        if square_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                SquareTokenRelationAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareTokenRelationAnalysisException.MSG,
                    err_code=SquareTokenRelationAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=square_validation_result.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        square = cast(Square, square_validation_result.payload)
        
        # Handle the case that, the token is not certified as safe.
        token_validation_result = token_validator.validate(candidate_satellite)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                SquareTokenRelationAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareTokenRelationAnalysisException.MSG,
                    err_code=SquareTokenRelationAnalysisException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_validation_result.exception,
                )
            )
        token = cast(Token, token_validation_result.payload)
        
        if (
                token.team.board != square.board or
                (
                        square.occupant != token and
                        token.current_position != square.coord
                )
        ):
            return AnalysisResult.success(RelationReport.no_relation())
        
        if square.occupant == token and token.current_position != square.coord:
            return AnalysisResult.success(RelationReport.stale_link(square))
        
        if square.occupant != token and token.current_position == square.coord:
            return AnalysisResult.success(RelationReport.registration_missing(square))
        
        return AnalysisResult.success(RelationReport.bidirectional(primary=square, satellite=token))