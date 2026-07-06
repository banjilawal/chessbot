# src/analyzer/relation/token/square/analyzer.py

"""
Module: analyzer.relation.token.square.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import RelationAnalyzer
from err import SquareTokenRelationAnalyzerException
from model import Square, Token
from report import RelationReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter
from validator import SquareValidator, TokenValidator


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
                    token_readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
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
            token_validator: TokenValidator | None = None,
            square_validator: SquareValidator | None = None,
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
            token_validator: TokenValidator
            square_validator: SquareValidator
        Returns:
            AnalysisResult[RelationReport]
        Raises:
            SquareTokenRelationAnalyzerException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        if square_validator is None:
            square_validator = SquareValidator()
        
        # Handle the case that, the square is not certified as safe.
        square_validation_result = square_validator.validate(candidate_primary)
        if square_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                SquareTokenRelationAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareTokenRelationAnalyzerException.MSG,
                    err_code=SquareTokenRelationAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=square_validation_result.exception,
                )
            )
        # Cast the validated primary as a Square.
        square = cast(Square, square_validation_result.payload)
        
        # Handle the case that, the token is flagged.
        token_validation_result = token_validator.execute(candidate_satellite)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                SquareTokenRelationAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareTokenRelationAnalyzerException.MSG,
                    err_code=SquareTokenRelationAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=token_validation_result.exception,
                )
            )
        # Cast the validated satellite as a Token.
        token = cast(Token, token_validation_result.payload)
        # --- Validations have been passed. Run the relation analysis steps. ---#
        
        # Case No Relation: Tokens and squares on different boards or without a common coord.
        if (
                token.team.board != square.board or
                (
                        square.occupant != token and
                        token.current_position != square.coord
                )
        ):
            return AnalysisResult.success(RelationReport.no_relation())
        
        # Case Stale Link: square has a token but their coords don't match.
        if square.occupant == token and token.current_position != square.coord:
            return AnalysisResult.success(RelationReport.stale_link(square))
        
        # Case Registration Missing: square does not have token but, token has square's coord.
        if square.occupant != token and token.current_position == square.coord:
            return AnalysisResult.success(RelationReport.registration_missing(square))
        
        # Case Fully Bidirectional: Square has token and token's coord matches square's
        return AnalysisResult.success(RelationReport.bidirectional(primary=square, satellite=token))