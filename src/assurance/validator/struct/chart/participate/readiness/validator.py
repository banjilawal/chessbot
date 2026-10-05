# src/assurance/validator/struct/chart/readiness/validator.py

"""
Module: assurance.validator.struct.chart.readiness.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit

from domain import CombatantToken, KingToken, Token
from err import DisabledTokenException, ParticipantReadinessValidatorException
from util import LoggingLevelRouter


class ParticipantReadinessValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        loader: TokenValidatorToolkit

    Provides:
        -   def execute(participant: Token) -> ValidationResult[Token]:

    Super Class:
    """
    _loader: TokenValidatorToolkit
    
    def __init__(
            self,
            loader: Optional[TokenValidatorToolkit] | None = None
    ):
        """
        Args:
            loader: Optional[TokenValidatorToolkit]
        """
        self._toolkit=toolkit or TokenValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(self, participation_candidate: Token) -> ValidationResult[Token]:
        """
        Assure a candidate's properties are reference for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_validator fails.
            2.  Otherwise, send a EncounterReadinessChart in the success result.
        Args:
            participation_candidate: Token
        Returns:
           ValidationResult[Token]
        Raises:
            EncounterReadinessCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        is_not_ready: bool = False
        token = participation_candidate
        # Handle the case that the participant is disabled from participating
        if isinstance(participation_candidate, KingToken):
            token = cast(KingToken, participation_candidate)
            is_not_ready = token.is_not_ready
        else:
            token = cast(CombatantToken, participation_candidate)
            is_not_ready = token.is_not_ready
        
        if token.is_not_ready:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipantReadinessValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipantReadinessValidatorException.MSG,
                    err_code=ParticipantReadinessValidatorException.ERR_CODE,
                    ex=DisabledTokenException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DisabledTokenException.MSG,
                        err_code=DisabledTokenException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(token)