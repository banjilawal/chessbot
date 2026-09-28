# src/assurance/validator/model/attack/validator.py

"""
Module: assurance.validator.model.attack.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import AttackValidatorToolkit, ModelValidator
from domain import Encounter
from transit import AttackCarrier
from util import LoggingLevelRouter


class AttackValidator(ModelValidator[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a AttackCarrier is safe to use.

    Attributes:
        toolkit: AttackValidatorToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[AttackCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[AttackValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AttackValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or AttackValidatorToolkit())
    
    @property
    def toolkit(self) -> AttackValidatorToolkit:
        return cast(AttackValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[AttackCarrier]:
        """
        Assure a candidate is a safe AttackCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The validation_router does not return a product
            2.  Otherwise, send a AttackCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AttackCarrier]
        Raises:
            AttackValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        table_generation_result = self._property_table_generator.execute(candidate=candidate)
        if table_generation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidatorException.MSG,
                    err_code=AttackValidatorException.ERR_CODE,
                    ex=table_generation_result.exception,
                )
            )
        common_property_table = cast(
            CommonAttackPropertyTable,
            table_generation_result.payload,
        )
        router_result = self._validation_router.execute()
        
        # --- Extract common Attack validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(AttackDeployment, deployment_validation.payload)
        position = position_log["position".upper()]
        
        # Handle the case that the router did not send a safe Attack.
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
                AttackValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidatorException.MSG,
                    err_code=AttackValidatorException.ERR_CODE,
                    ex=router_result.exception,
                )
            )
        # --- Send the work product. ---#
        safe_carrier = cast(AttackCarrier, router_result.payload)
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
            AttackValidatorException
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
                AttackValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidatorException.MSG,
                    err_code=AttackValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product. ---#
        coord = cast(Coord, result.payload)
        return ValidationResult.success(coord)
    