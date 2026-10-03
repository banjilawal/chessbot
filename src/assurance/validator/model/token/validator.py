# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import (
    TokenValidationReference, RootTokenValidator, ModelValidator, TokenPositionChartValidator,
    TokenValidationRouter,
    TokenValidatorToolkit
)
from domain import Coord, Formation, HomeSquare, Token, TokenBlueprint, TokenDeployment, TokenPrimeExtract
from err import FormationNullException, TokenDeploymentNullException, TokenValidatorException
from exchange import TeamValidationRequest
from transit import TeamCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier is safe to use.

    Attributes:
        toolkit: TokenValidatorToolkit
        validation_router: TokenValidationRouter
        property_table_generator: TokenValidationReferenceGenerator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    _validation_router: TokenValidationRouter
    _property_table_generator: RootTokenValidator
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            validation_router: Optional[TokenValidationRouter] | None = None,
            property_table_generator: Optional[RootTokenValidator]
                                      | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            validation_router: Optional[TokenValidationRouter]
            property_table_generator: Optional[TokenValidationReferenceGenerator]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._validation_router = validation_router or TokenValidationRouter()
        self._property_table_generator = (
                property_table_generator or
                RootTokenValidator()
        )
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The validation_router does not return a product
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        table_generation_result = self._property_table_generator.execute(candidate=candidate)
        if table_generation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=table_generation_result.exception,
                )
            )
        common_property_table = cast(
            TokenValidationReference,
            table_generation_result.payload,
        )
        router_result = self._validation_router.execute()
        
        # --- Extract common Token validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        position = position_log["position".upper()]
        
        # Handle the case that the router did not send a safe Token.
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
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=router_result.exception,
                )
            )
        # --- Send the work product. ---#
        safe_carrier = cast(TokenCarrier, router_result.payload)
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
            TokenValidatorException
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
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product. ---#
        coord = cast(Coord, result.payload)
        return ValidationResult.success(coord)
    