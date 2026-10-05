# src/assurance/validator/struct/chain/participate/validator.py

"""
Module: assurance.validator.struct.chain.participate.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from artifcat import ValidationResult
from assurance import (
    ChartValidator, ParticipantReadinessValidator,
    ParticipationValidatorToolkit
)
from domain import (
    Participation, ParticipationBlueprint, ParticipationPrimeExtract,
    Token
)
from err import (
    FriendlyFireAttackException, ParticipationCarrierEmptyException,
    ParticipationValidatorException, TokenAttackingItselfException,
    VictimNeverDeployedException
)
from exchange import TokenValidationRequest
from transit import ParticipationCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class ParticipationValidator(ChartValidator[Participation]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        toolkit: ParticipationValidatorToolkit
        readiness_validator: ParticipantReadinessValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[[ParticipationCarrier]:

    Super Class:
        ChartValidator
    """
    _readiness_validator: ParticipantReadinessValidator
    
    def __init__(
            self,
            toolkit: Optional[ParticipationValidatorToolkit] | None = None,
            readiness_validator: Optional[ParticipantReadinessValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ParticipationValidatorToolkit]
            readiness_validator: Optional[ParticipantReadinessValidator]
        """
        super().__init__(toolkit=toolkit or ParticipationValidatorToolkit())
        self._readiness_validator = readiness_validator or ParticipantReadinessValidator()
    
    @property
    def toolkit(self) -> ParticipationValidatorToolkit:
        return cast(ParticipationValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ParticipationCarrier]:
        """
        Assure a candidate is a safe ParticipationCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   Loader fails.
                    -   The ParticipationBlueprint has an inconsistency.
                    -   The CoordValidator flags either existing position.
            2.  Otherwise, send the type of carrier prime_extract indicates.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Participation]
        Raises:
            ParticipationValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidatorException.MSG,
                    err_code=ParticipationValidatorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(ParticipationPrimeExtract, load_result.payload)
        carrier = prime_extract.carrier
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidatorException.MSG,
                    err_code=ParticipationValidatorException.ERR_CODE,
                    ex=ParticipationCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipationCarrierEmptyException.MSG,
                        err_code=ParticipationCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        
        tokens: List[Token] = []
        for token in [blueprint.victim, blueprint.attacker]:
            token_validation = self.toolkit.wrapper.token.extract_model(
                request=TokenValidationRequest(
                    item=TokenCarrier(model=token),
                    id=IdFactory.next_id(class_name="TokenValidationRequest"),
                )
            )
            if token_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    ParticipationValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipationValidatorException.MSG,
                        err_code=ParticipationValidatorException.ERR_CODE,
                        ex=token_validation.exception,
                    )
                )
            tokens.append(cast(Token, token_validation.payload))
        victim = tokens[0]
        attacker = tokens[1]
        
        # Handle the case that the victim and the attacker are the same
        if victim == attacker:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidatorException.MSG,
                    err_code=ParticipationValidatorException.ERR_CODE,
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
                ParticipationValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidatorException.MSG,
                    err_code=ParticipationValidatorException.ERR_CODE,
                    ex=FriendlyFireAttackException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FriendlyFireAttackException.MSG,
                        err_code=FriendlyFireAttackException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that either token has never been deployed.
        for token in [victim, attacker]:
            if token.has_never_been_deployed:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    ParticipationValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipationValidatorException.MSG,
                        err_code=ParticipationValidatorException.ERR_CODE,
                        ex=VictimNeverDeployedException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=VictimNeverDeployedException.MSG,
                            err_code=VictimNeverDeployedException.ERR_CODE,
                        ),
                    )
                )
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        # The client wants safe Participants.
        if prime_extract.recipient_wants_model:
            payload = ParticipationCarrier(
                model=Participation(
                    victim=victim,
                    attacker=attacker,
                )
            )
            return ValidationResult.success(payload)
        # Otherwise, the client is a ParticipationBuilder that needs a Blueprint.
        payload = ParticipationCarrier(
            blueprint=ParticipationBlueprint(
                victim=victim,
                attacker=attacker,
            )
        )
        return ValidationResult.success(payload)
        # --- Send the work product. ---#