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
from validation import RankValidator


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
            

        # --- Send the work product. ---#
        return AnalysisResult.completed(RankLevelApproval.approve(new_rank))
