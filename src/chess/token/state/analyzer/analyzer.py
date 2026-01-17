# src/chess/token/state/analyzer.py

"""
Module: chess.token.state.analyzer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.token import NullTokenStateException, Token, TokenService, TokenState, TokenStateAnalysisFailedException
from chess.system import RelationAnalyzer, RelationReport


class TokenStateAnalyzer(RelationAnalyzer[TokenState, Token]):
    
    @classmethod
    def analyze(
            cls,
            candidate_satellite: Token,
            candidate_primary: TokenState,
            token_service: TokenService = TokenService(),
    ) -> RelationReport[TokenState, Token]:
        """"""
        method = "TokenStateAnalyzer.analyze"
        
        # Handle the case that the candidate_primary does not exist.
        if candidate_primary is None:
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenStateException(f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate_primary is the wrong type.
        if not isinstance(candidate_primary, TokenState):
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected TokenState, got {type(candidate_primary).__name__} instead.")
                )
            )
        # Handle the case that the candidate_satellites is not certified.
        token_validation = token_service.validator.validate(candidate=candidate_satellite)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=token_validation.exception
                )
            )
        if