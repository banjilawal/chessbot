# src/bootstrap/validator/readiness/bootstrapper.py

"""
Module: bootstrap.validator.readiness.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bootstrap import ValidatorBootstrapper
from err import ReadinessValidatorBootstrapperException
from model import CombatantToken, KingToken, Token
from report import TokenReadinessReport
from result import ValidationResult
from toolkit import ReadinessValidatorBootstrapperToolkit
from util import LoggingLevelRouter
from validation import TokenValidator


class ReadinessValidatorBootstrapper(ValidatorBootstrapper):
    """
    Role:
        -   Analysis Factory
        -   Consistency maintenance


    Responsibilities:
        1.  Analyze a token's aliveness before its used in the brought into play.
        2.  Combine safety and aliveness tests unique to each subclass under one roof.

    Attributes:

    Provides:
        -   validator(
                    token: Token,
                    token_validator: TokenValidator,
            ) -> ValidationResult[TokenFreedomReport]

    Parent:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            subject: Token,
            toolkit: ReadinessValidatorBootstrapperToolkit | None = None
    ) -> ValidationResult[TokenReadinessReport]:
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
            toolkit: ReadinessValidatorBootstrapperToolkit
        Returns:
              ValidationResult[TokenFreedomReport]
        Raises:
            TokenFreedomValidatorException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ReadinessValidatorBootstrapperToolkit()
        
        # Handle the case that, the token does not pass a validation check.
        validation_result = toolkit.token_validator.validate(subject)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return ValidationResult.failure(
                ReadinessValidatorBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ReadinessValidatorBootstrapperException.MSG,
                    err_code=ReadinessValidatorBootstrapperException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # Deal with the simplest universal case first, token has no been deployed.
        if subject.is_not_deployed:
            return ValidationResult.completed(TokenReadinessReport.inactive(subject))

        if isinstance(subject, CombatantToken):
            return toolkit.combatant_readiness_validator.analyze(
                subject=cast(CombatantToken, subject)
            )
        return toolkit.king_readiness_validator.analyze(
            subject=cast(KingToken, subject)
        )