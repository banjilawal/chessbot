# src/validator/model/game/validator.py

"""
Module: validator.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import GameValidatorToolkit, ModelValidator
from config import NumericSetting
from domain import (
    Game, GameBlueprint, GameValidationRequest, Path, PathValidationRequest,
    Token, TokenValidationRequest
)
from err import (
    EmptyGameCarrierException, EmptyPathCarrierException, EmptyTokenCarrierException,
    GameValidationRequestNullException, GameValidatorException
)

from artifcat import ValidationResult
from transit import GameCarrier, PathCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class GameValidator(ModelValidator[Game]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a GameCarrier and its contents are safe before use.

    Attributes:
        toolkit: GameValidatorToolkit

    Provides:
        *   def execute(candidate: Any) -> ValidationResult[GameCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[GameValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[GameValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or GameValidatorToolkit())
    
    @property
    def toolkit(self) -> GameValidatorToolkit:
        return cast(GameValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[GameCarrier]:
        """
        Certify a GameCarrier's payload is either a Game or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    *   The request is either null or not a GameValidatorRequest.
                    *   The request's payload is either,
                            null
                            not a GameCarrier
                            an empty GameCarrier.
                    *   Either the id, token, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
            GameValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=GameValidationRequest,
            null_exception=GameValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        request = cast(GameValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Extract the blueprint from the validated carrier. ---#
        carrier = cast(GameCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        # Handle the case that the carrier does not produce a Blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=EmptyGameCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyGameCarrierException.MSG,
                        err_code=EmptyGameCarrierException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        benefit_validation = self.toolkit.helper.number_validator.execute(
            candidate=blueprint.benefit,
            floor=NumericSetting().negative_infinity,
            ceiling=NumericSetting().infinity,
        )
        if benefit_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=benefit_validation.exception,
                )
            )
        # Handle the case that the traveler does not pass a validation check.
        traveler_validation = self.toolkit.helper.path_validator.execute(
            candidate=TokenValidationRequest(
                item=TokenCarrier(model=blueprint.traveler),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            ),
        )
        if traveler_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=traveler_validation.exception,
                )
            )
        # --- Extract the traveler validation payload. ---#
        traveler_carrier = cast(TokenCarrier, traveler_validation.payload)
        traveler_blueprint = traveler_carrier.extract_blueprint()
        # Handle the case that the traveler_blueprint is null.
        if traveler_blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=EmptyTokenCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyTokenCarrierException.MSG,
                        err_code=EmptyTokenCarrierException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the traveler_blueprint does not contain a model.
        # --- Run the path validation checks. ---#
        path_validation = self.toolkit.helper.path_validator.execute(
            candidate=PathValidationRequest(
                item=PathCarrier(model=blueprint.path),
                id=IdFactory.next_id(class_name="PathValidationRequest"),

            )
        )
        # Handle the case that the path is flagged.
        if path_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=path_validation.exception,
                )
            )
        # --- Extract the path validation payload. ---#
        path_carrier = cast(PathCarrier, path_validation.payload)
        path_blueprint = path_carrier.extract_blueprint()
        # Handle the case that the traveler_blueprint is null.
        if path_blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=EmptyPathCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPathCarrierException.MSG,
                        err_code=EmptyPathCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Extract validation payloads. ---#
        benefit = cast(int, benefit_validation.payload)
        traveler = cast(Token, traveler_carrier.entity)
        path = cast(Path, path_carrier.entity)
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.is_carrying_model:
            payload = Game(benefit=benefit, traveler=traveler, path=path)
            return ValidationResult.success(GameCarrier(model=payload))
        # The blueprint case
        payload = GameBlueprint(benefit=benefit, traveler=traveler, path=path)
        return ValidationResult.success(GameCarrier(blueprint=payload))
        
        
