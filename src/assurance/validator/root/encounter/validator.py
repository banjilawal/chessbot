# src/assurance/validator/validator/root/encounter/generator.py

"""
Module: assurance.validator.root.encounter.generator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import EncounterLoader, EncounterValidatorToolkit, RootValidator
from config import NumericSetting
from domain import (
    Encounter, EncounterPrimeExtract, Maneuver, Participation,
    ParticipationBlueprint, Token
)
from err import EncounterCarrierEmptyException, RootEncounterValidatorException
from exchange import (
    ManeuverValidationRequest, ParticipationValidationRequest,
    TokenValidationRequest
)
from transit import (
    ManeuverCarrier, ParticipationCarrier, RootEncounterEnvelope, TokenCarrier
)
from util import IdFactory, LoggingLevelRouter


class RootEncounterValidator(RootValidator[Encounter]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Encounter super class, then send a 
            RootEncounterEnvelope for additional processing.

    Attributes:
        loader: EncounterLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootEncounterEnvelope]

    Super Class:
        RootValidator
    """
    
    def __init__(
            self,
            loader: Optional[EncounterLoader] | None = None
    ):
        """
        Args:
            loader: Optional[EncounterLoader]
        """
        super().__init__(loader=loader or EncounterLoader())
    
    @property
    def loader(self) -> EncounterLoader:
        return cast(EncounterLoader, super().loader)
    
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RootEncounterEnvelope]:
        """
        Assure a candidate's properties are reference for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a RootEncounterEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[RootEncounterEnvelope]
        Raises:
            RootEncounterEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(EncounterPrimeExtract, loading.payload)
        carrier = prime_extract.carrier
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_ID_ATTRIBUTE. ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self.toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- PROCESS_THE_VICTIM_ATTRIBUTE. ---#
        
        # Handle the case that the victim is flagged.
        victim_validation = self.toolkit.wrapper.token.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=blueprint.victim),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            )
        )
        if victim_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=victim_validation.exception,
                )
            )
        # --- PROCESS_THE_ATTACKER_MANEUVER_ATTRIBUTE. ---#
        # Handle the case that the token is flagged.
        attacker_maneuver_validation = self.toolkit.wrapper.maneuver.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=blueprint.attacker_maneuver),
                id=IdFactory.next_id(class_name="TManeuverValidationRequest"),
            )
        )
        if attacker_maneuver_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=attacker_maneuver_validation.exception,
                )
            )
        # --- PROCESS_THE_ATTACKER_REWARD_ATTRIBUTE. ---#
        attacker_reward = self.toolkit.number_validator.execute(
            candidate=blueprint.attacker_reward,
            floor=NumericSetting.floor(),
            ceiling=NumericSetting.ceiling(),
        )
        
        if attacker_reward.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=attacker_reward.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        victim = cast(Token, victim_validation.payload)
        attacker_reward = cast(int, attacker_reward.payload)
        attacker_maneuver = cast(Maneuver, attacker_maneuver_validation.payload)
        
        participation_validation = self.toolkit.wrapper.participation.extract_blueprint(
            request=ParticipationValidationRequest(
                item=ParticipationCarrier(
                    blueprint=ParticipationBlueprint(
                        victim=victim,
                        attacker=attacker_maneuver.traveler,
                    )
                ),
                id=IdFactory.next_id(class_name="ParticipationValidationRequest")
            )
        )
        if participation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootEncounterValidatorException.MSG,
                    err_code=RootEncounterValidatorException.ERR_CODE,
                    ex=participation_validation.exception
                )
            )
        participation_blueprint = cast(
            ParticipationBlueprint,
            participation_validation.payload,
        )
        participants = Participation(
            victim=participation_blueprint.victim,
            attacker=participation_blueprint.attacker,
        )
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootEncounterEnvelope(
            id=id,
            participants=participants,
            attacker_reward=attacker_reward,
            attacker_maneuver=attacker_maneuver,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    