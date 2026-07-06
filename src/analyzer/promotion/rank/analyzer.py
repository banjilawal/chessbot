# src/analyzer/promotion/rank/analyzer.py

"""
Module: analyzer.promotion.rank.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from err import PromoteToKingException, PromoteToPawnException, PromotionLevelAnalyzerException
from model import King, Pawn, Rank
from report import RankLevelApproval
from result import AnalysisResult
from util import LoggingLevelRouter
from validator import RankValidator


class PromotionRankAnalyzer(Analyzer):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Perform safety and bounds checks on a pawn's requested new rank.

    Attributes:

    Properties:
        -   def analyze(
                    new_rank: Rank,
                    rank_validator: RankValidator,
            ) -> AnalysisResult[PromotionLevelReport]:

    Super Class:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            new_rank: Rank,
            rank_validator: RankValidator | None = None,
    ) -> AnalysisResult[RankLevelApproval]:
        """
        Verify the pawn's new Rank is not Pawn or King..
        
        Action:
            1.  Send an exception in the AnalysisResult any of these
                conditions occur.
                    -   Is flagged by rank_validator
                    -   The new rank is either Pawn or King.
            3.  Otherwise, Send the success result.
        Args:
            new_rank: Rank
            rank_validator: RankValidator
        Returns:
            AnalysisResult[PromotionLevelReport]
        Raises:
            PromotionLevelAnalyzerException
            PromoteToKingException
            PromoteToPawnException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if rank_validator is None:
            rank_validator = RankValidator()
            
        # Handle the case that, the candidate is flagged by the rank_validator.
        validation_result = rank_validator.execute(new_rank)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                PromotionLevelAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PromotionLevelAnalyzerException.MSG,
                    err_code=PromotionLevelAnalyzerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the higher rank is a King's.
        if isinstance(new_rank, King):
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                RankLevelApproval.deny(
                    exception=PromoteToKingException(
                        msg=PromoteToKingException.MSG,
                        err_code=PromoteToKingException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the new rank is still a Pawn's.
        if isinstance(new_rank, Pawn):
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                RankLevelApproval.deny(
                    exception=PromoteToPawnException(
                        msg=PromoteToPawnException.MSG,
                        err_code=PromoteToPawnException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return AnalysisResult.completed(RankLevelApproval.approve(new_rank))
