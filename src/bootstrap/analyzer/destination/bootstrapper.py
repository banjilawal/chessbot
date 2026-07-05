# src/bootstrap/analyzer/destination/bootstrapper.py

"""
Module: bootstrap.analyzer.destination.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bootstrap import AnalyzerBootstrapper
from err import DestinationAnalyzerBootstrapperException
from model import CombatantToken, KingToken, Token
from report import TokenDestinationReport
from result import AnalysisResult
from toolkit import DestinationAnalyzerBootstrapperToolkit
from util import LoggingLevelRouter
from validation import TokenValidator


class DestinationAnalyzerBootstrapper(AnalyzerBootstrapper):
    """
    Role:
        -   Analysis Factory
        -   Consistency maintenance


    Responsibilities:
        1.  Analyze a token's aliveness before its used in the brought into play.
        2.  Combine safety and aliveness tests unique to each subclass under one roof.

    Attributes:

    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenValidator,
            ) -> AnalysisResult[TokenFreedomReport]

    Parent:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            subject: Token,
            toolkit: DestinationAnalyzerBootstrapperToolkit | None = None
    ) -> AnalysisResult[TokenDestinationReport]:
        """
        MAke sure the token can be used.

        Action:
            1.  If the token fails, its certification, send an exception chain in the
                RelationReport.
            2.  Otherwise, decide if the token is actionable based on.
                    -   if it has been deployed.
                    -   It has not been captured or checkmated.
            3.  Send the success result.

        Args:
            subject: Token
            toolkit: DestinationAnalyzerBootstrapperToolkit
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
            TokenFreedomAnalyzerException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = DestinationAnalyzerBootstrapperToolkit()
        
        # Handle the case that, the token does not pass a validation check.
        validation_result = toolkit.token_validator.validate(subject)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return AnalysisResult.failure(
                DestinationAnalyzerBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=DestinationAnalyzerBootstrapperException.MSG,
                    err_code=DestinationAnalyzerBootstrapperException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # Deal with the simplest universal case first, token has no been deployed.
        if subject.is_not_deployed:
            return AnalysisResult.completed(TokenDestinationReport.inactive(subject))

        if isinstance(subject, CombatantToken):
            return toolkit.combatant_destination_analyzer.analyze(
                subject=cast(CombatantToken, subject)
            )
        return toolkit.king_destination_analyzer.analyze(
            subject=cast(KingToken, subject)
        )