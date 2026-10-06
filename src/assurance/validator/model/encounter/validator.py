# src/assurance/validator/model/encounter/validator.py

"""
Module: assurance.validator.model.encounter.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import (
    RootEncounterEnvelope, RootEncounterEnvelopeGenerator, ModelValidator,
    EncounterPositionTableGenerator,
    EncounterValidationRouter,
    EncounterValidatorToolkit, RootEncounterEnvelopeProducer
)
from domain import Coord, Formation, HomeSquare, Encounter, EncounterBlueprint, EncounterDeployment, EncounterPrimeExtract
from err import FormationNullException, EncounterDeploymentNullException, EncounterValidatorException
from exchange import TeamValidationRequest
from transit import RootEncounterEnvelope, TeamCarrier, EncounterCarrier
from util import IdFactory, LoggingLevelRouter


class EncounterValidator(ModelValidator[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a EncounterCarrier is safe to use.

    Attributes:
        loader: EncounterValidatorToolkit
        validation_router: EncounterValidationRouter
        property_table_generator: RootEncounterEnvelopeGenerator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[EncounterCarrier]:

    Super Class:
        ModelValidator
    """
    _validation_router: EncounterValidationRouter
    _root_validator: RootEncounterEnvelopeProducer
    
    def __init__(
            self,
            root_validator: Optional[RootEncounterEnvelopeProducer] | None = None,
            loader: Optional[EncounterValidatorToolkit] | None = None,
            validation_router: Optional[EncounterValidationRouter] | None = None,
            property_table_generator: Optional[RootEncounterEnvelopeGenerator]
                                      | None = None,
    ):
        """
        Args:
            loader: Optional[EncounterValidatorToolkit]
            validation_router: Optional[EncounterValidationRouter]
            property_table_generator: Optional[RootEncounterEnvelopeGenerator]
        """
        super().__init__(toolkit=toolkit or EncounterValidatorToolkit())
        self._validation_router = validation_router or EncounterValidationRouter()
        self._property_table_generator = (
                property_table_generator or
                RootEncounterEnvelopeGenerator()
        )
        self._root_validator = root_validator
    
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return cast(EncounterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[EncounterCarrier]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The validation_router does not return a product
            2.  Otherwise, send a EncounterCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
            EncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        root_validation = self._root_validator.execute(candidate=candidate)
        if root_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=root_validation.exception,
                )
            )
        envelope = cast(RootEncounterEnvelope, root_validation.payload)
        routing_result = self._validation_router.execute(enveloper=envelope)
        # Handle the case that the blueprint cannot be extracted.
        table_generation_result = self._property_table_generator.execute(candidate=candidate)
        if table_generation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=table_generation_result.exception,
                )
            )
        common_property_table = cast(
            RootEncounterEnvelope,
            table_generation_result.payload,
        )
        router_result = self._validation_router.execute()
        
        # --- Extract common Encounter validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(EncounterDeployment, deployment_validation.payload)
        position = position_log["position".upper()]
        
        # Handle the case that the router did not send a safe Encounter.
        router_result = self._validation_router.execute(
            id=id,
            team=team,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            position=position,
            previous_position,
            prime_extract=prime_extract,
        )
        if router_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=router_result.exception,
                )
            )
        # --- Send the work product. ---#
        safe_carrier = cast(EncounterCarrier, router_result.payload)
        return ValidationResult.success(safe_carrier)
    
    @LoggingLevelRouter.monitor
    def _position_validator(self, position_candidate: Any) -> ValidationResult[Coord]:
        """
        Assure a not-null position is a safe Coord.

        Action:
            1.  Send an exception chain in the ValidationResult if the
                candidate is flagged.
            2.  Otherwise, send a Coord in the success result.
        Args:
            position_candidate: Any
        Returns:
            ValidationResult[Coord]
        Raises:
            EncounterValidatorException
        """
        method = f"{self.__class__.__name__}._position_validator"
        
        result = self.toolkit.wrapper.coord.extract_model(
            request=CoordValidationRequest(
                item=CoordCarrier(model=position_candidate),
                id=IdFactory.next_id(class_name="CoordValidationRequest"),
            )
        )
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidatorException.MSG,
                    err_code=EncounterValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product. ---#
        coord = cast(Coord, result.payload)
        return ValidationResult.success(coord)
    