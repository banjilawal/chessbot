# src/assurance/validator/validator/root/encounter/participant/validator.py

"""
Module: assurance.validator.root.encounter.participant.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import ValidationResult
from assurance import (
    EncounterParticipants, ParticipantReadinessValidator, TokenValidatorToolkit
)
from domain import Token
from err import (
    EncounterParticipantValidatorException, FriendlyFireAttackException,
    TokenAttackingItselfException, VictimNeverDeployedException
)
from util import LoggingLevelRouter


class EncounterParticipantValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        toolkit: TokenValidatorToolkit
        readiness_validator: ParticipantReadinessValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[EncounterParticipantChart]:

    Super Class:
        VerificationProducer
    """
    _readiness_validator: ParticipantReadinessValidator
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            readiness_validator: Optional[ParticipantReadinessValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            readiness_validator: Optional[ParticipantReadinessValidator]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._readiness_validator = readiness_validator or ParticipantReadinessValidator()
        
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            victim: Token,
            attacker: Token
    ) -> ValidationResult[EncounterParticipants]:
        """
        Assure a candidate's properties are reference for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_validator fails.
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
                EncounterParticipantValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantValidatorException.MSG,
                    err_code=EncounterParticipantValidatorException.ERR_CODE,
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
                EncounterParticipantValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantValidatorException.MSG,
                    err_code=EncounterParticipantValidatorException.ERR_CODE,
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
                EncounterParticipantValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterParticipantValidatorException.MSG,
                    err_code=EncounterParticipantValidatorException.ERR_CODE,
                    ex=VictimNeverDeployedException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VictimNeverDeployedException.MSG,
                        err_code=VictimNeverDeployedException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that either participant is not ready
        participants: List[Token] = []
        for candidate in [victim, attacker]:
            readiness_validation = self._readiness_validator.execute(candidate)
            if readiness_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterParticipantValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterParticipantValidatorException.MSG,
                        err_code=EncounterParticipantValidatorException.ERR_CODE,
                        ex=readiness_validation.exception,
                    )
                )
            participants.append(cast(Token, readiness_validation.payload))
        # --- Send the work product. ---#
        participant_chart = EncounterParticipants(
            victim=participants[0],
            attacker=participants[1],
        )
        return ValidationResult.success(participant_chart)

    