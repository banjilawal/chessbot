# src/assurance/reference/charter/chart/encounter/charter.py

"""
Module: assurance.reference.charter.chart.encounter.charter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from artifcat import ValidationResult
from assurance import EncounterParticipantChart, TokenValidatorToolkit, VerificationCharter
from domain import Encounter, Token
from err import FriendlyFireAttackException, TokenAttackingItselfException, VictimNeverDeployedException
from sensor import FriendshipAnalyzer
from util import IdFactory, LoggingLevelRouter


class EncounterParticipantStateCertifier(VerificationCharter[Encounter]):
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
            victim_candidate: Token,
            attacker_candidate: Token
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
            candidate: Any
        Returns:
           ValidationResult[EncounterParticipantChart]
        Raises:
            EncounterVerificationCharterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the victim and the attacker are the same
        if victim_candidate == attacker_candidate:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterVerificationCharterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterVerificationCharterException.MSG,
                    err_code=EncounterVerificationCharterException.ERR_CODE,
                    ex=TokenAttackingItselfException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenAttackingItselfException.MSG,
                        err_code=TokenAttackingItselfException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the victim and attacker are on the same team.
        if victim_candidate.is_friend(attacker_candidate):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterVerificationCharterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterVerificationCharterException.MSG,
                    err_code=EncounterVerificationCharterException.ERR_CODE,
                    ex=FriendlyFireAttackException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FriendlyFireAttackException.MSG,
                        err_code=FriendlyFireAttackException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the victim has never been deployed.
        if victim_candidate.has_never_been_deployed:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterVerificationCharterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterVerificationCharterException.MSG,
                    err_code=EncounterVerificationCharterException.ERR_CODE,
                    ex=VictimNeverDeployedException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VictimNeverDeployedException.MSG,
                        err_code=VictimNeverDeployedException.ERR_CODE,
                    ),
                )
            )
            
        reference_properties = EncounterReferencePropertyTable(
            victim=cast(Token, victim_candidate),
            attacker=(Token, attacker_candidate)
        )
        # --- Send the work product. ---#
        participant_chart: EncounterParticipantChart = EncounterParticipantChart(
            victim=victim, attacker=attacker,
        )# --- Send the work product. -- =
        return ValidationResult.success(participant_chart)

    