# src/assurance/validator/model/encounter/position/validator.py

"""
Module: assurance.validator.model.encounter.position.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from artifcat import ValidationResult
from assurance import EncounterPositionTable, EncounterValidatorToolkit
from domain import Coord, EncounterBlueprint
from err import EncounterPositionTableGeneratorException
from exchange import CoordValidationRequest
from transit import CoordCarrier
from util import IdFactory, LoggingLevelRouter


class EncounterPositionTableGenerator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a EncounterBlueprint position and previous_positions fields
            are safe to use.

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(
                    blueprint: EncounterBlueprint
            ) -> ValidationResult[EncounterPositionTable]:

    Super Class:
    """
    _toolkit: EncounterValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
        """
        self._toolkit = toolkit or EncounterValidatorToolkit()

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: EncounterBlueprint,
    ) -> ValidationResult[EncounterPositionTable]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if either
                    -   blueprint.position or
                    -   blueprint.previous_postion
                is not null and gets flagged.
            2.  Otherwise, for the success result, send a dictionary that is:
                    -   Empty if the Encounter has not been deployed.
                    -   Any validated position.
        Args:
            blueprint: EncounterBlueprint
        Returns:
            ValidationResult[EncounterPositionTable]
        Raises:
            EncounterPositionValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        valid_locations: Dict[str, Coord] = {}
        # If the encounter has not been deployed send an empty dictionary
        if (
                blueprint.position is None and 
                blueprint.previous_position is None
        ):
            return ValidationResult.success(valid_locations)
        
        if blueprint.position is not None:
            # Handle the case that the position is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.position),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterPositionTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterPositionTableGeneratorException.MSG,
                        err_code=EncounterPositionTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["position"] = cast(Coord, validation.payload)
        
        if blueprint.previous_position is not None:
            # Handle the case that the previous position is flagged.
            validation = self._toolkit.wrapper.coord.extract_model(
                request=CoordValidationRequest(
                    item=CoordCarrier(model=blueprint.previous_position),
                    id=IdFactory.next_id(class_name="CoordValidationRequest"),
                )
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterPositionTableGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterPositionTableGeneratorException.MSG,
                        err_code=EncounterPositionTableGeneratorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            # Otherwise add to the dictionary.
            valid_locations["previous_position"] = cast(Coord, validation.payload)
        # --- Send the work product. ---#
        position_table = EncounterPositionTable(
            position=valid_locations["position"] or None,
            previous_position=valid_locations["previous_position"] or None,
        )
        return ValidationResult.success(position_table)
    