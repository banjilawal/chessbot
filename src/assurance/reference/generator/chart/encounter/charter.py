# src/assurance/reference/charter/chart/encounter/charter.py

"""
Module: assurance.reference.charter.chart.encounter.charter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import EncounterParticipantChart, TokenValidatorToolkit, VerificationCharter
from domain import Encounter, Token
from err import (
    EncounterParticipantCertifierException, FriendlyFireAttackException, TokenAttackingItselfException,
    VictimNeverDeployedException
)
from util import LoggingLevelRouter


class EncounterParticipantCertifier(VerificationCharter[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        toolkit: TokenValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[EncounterParticipantChart]:

    Super Class:
        VerificationCharter
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            victim: Token,
            attacker: Token
    ) -> ValidationResult[EncounterParticipantChart]:
        """
        Assure a candidate's properties are reference for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_charter fails.
            2.  Otherwise, send a EncounterParticipantChart in the success result.
        Args:
            victim: Token
            attacker: Token
        Returns:
           ValidationResult[EncounterParticipantChart]
        Raises:
            EncounterParticipantCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the victim and the attacker are the same
        if victim == attacker:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterParticipantCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantCertifierException.MSG,
                    err_code=EncounterParticipantCertifierException.ERR_CODE,
                    ex=TokenAttackingItselfException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenAttackingItselfException.MSG,
                        err_code=TokenAttackingItselfException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the victim and attacker are on the same team.
        if victim.is_friend(attacker):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterParticipantCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantCertifierException.MSG,
                    err_code=EncounterParticipantCertifierException.ERR_CODE,
                    ex=FriendlyFireAttackException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FriendlyFireAttackException.MSG,
                        err_code=FriendlyFireAttackException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the victim has never been deployed.
        if victim.has_never_been_deployed:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterParticipantCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantCertifierException.MSG,
                    err_code=EncounterParticipantCertifierException.ERR_CODE,
                    ex=VictimNeverDeployedException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VictimNeverDeployedException.MSG,
                        err_code=VictimNeverDeployedException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        participant_chart = EncounterParticipantChart(
            victim=victim,
            attacker=attacker,
        )
        return ValidationResult.success(participant_chart)

    