# src/assurance/validator/model/encounter/participant/validator.py

"""
Module: assurance.validator.model.encounter.participant.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit
from domain import Token
from util import LoggingLevelRouter


class EncounterParticipantValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a EncounterBlueprint participant and previous_participants fields
            are safe to use.

    Attributes:
        loader: TokenValidatorToolkit

    Provides:
        -   def execute(
                    blueprint: EncounterBlueprint
            ) -> ValidationResult[EncounterParticipantTable]:

    Super Class:
    """
    _loader: TokenValidatorToolkit
    
    def __init__(
            self,
            loader: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenValidatorToolkit]
        """
        self._toolkit = toolkit or TokenValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            victim_candidate: Token,
            attacker_candidate: Token,
    ) -> ValidationResult[EncounterParticipantTable]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   blueprint.participant or
                    -   blueprint.previous_postion
                is not null and gets flagged.
            2.  Otherwise, for the success result, send a dictionary that is:
                    -   Empty if the Encounter has not been deployed.
                    -   Any validated participant.
        Args:
            blueprint: EncounterBlueprint
        Returns:
            ValidationResult[EncounterParticipantTable]
        Raises:
            EncounterParticipantValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        candidates: Dict[str, Token] = {}
        # If the encounter has not been deployed send an empty dictionary
        if (
                blueprint.participant is None and 
                blueprint.previous_participant is None
        ):
            return ValidationResult.success(valid_locations)
        
        if blueprint.participant is not None:
            # Handle the case that the participant is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.participant),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterParticipantTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterParticipantTableGeneratorException.MSG,
                        err_code=EncounterParticipantTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["participant"] = cast(Coord, validation.payload)
        
        if blueprint.previous_participant is not None:
            # Handle the case that the previous participant is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.previous_participant),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterParticipantTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterParticipantTableGeneratorException.MSG,
                        err_code=EncounterParticipantTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["previous_participant"] = cast(Coord, validation.payload)
        # --- Send the work product. ---#
        participant_table = EncounterParticipantTable(
            participant=valid_locations["participant"] or None,
            previous_participant=valid_locations["previous_participant"] or None,
        )
        return ValidationResult.success(participant_table)
    