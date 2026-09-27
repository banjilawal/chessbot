# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, TokenValidationRouter, TokenValidatorToolkit
from domain import (
    Coord, Formation, HomeSquare, Team, Token, TokenBlueprint, TokenDeployment,
    TokenPrimeExtract
)
from err import (
    CoordValidatorException, FormationNullException, TokenDeploymentNullException, TokenValidatorException
)
from exchange import CoordValidationRequest, TeamValidationRequest
from transit import CoordCarrier, TeamCarrier, TokenCarrier
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

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    _validation_router: TokenValidationRouter
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            validation_router: Optional[TokenValidationRouter] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            validation_router: Optional[TokenValidationRouter]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._validation_router = validation_router or TokenValidationRouter()
    
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
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, load_result.payload)
        token_blueprint = cast(TokenBlueprint, prime_extract.blueprint)
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=token_blueprint,
            blueprint_owner_name=token_blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self._toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the formation is flagged.
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that the deployment is flagged..
        deployment_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.deployment,
            target_model=TokenDeployment,
            null_exception=TokenDeploymentNullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # Handle the case that the team is flagged.
        team_validation = self.toolkit.wrapper.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=token_blueprint.team),
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
            )
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.home_square_extractor.execute(
            blueprint=token_blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # Handle the case that the current_position is flagged.
        position_validation: ValidationResult = ValidationResult.failure(
            CoordValidatorException()
        )
        if token_blueprint.position is not None:
            position_validation = self._position_validator(
                position_candidate=token_blueprint.position
            )
            if position_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenValidatorException.MSG,
                        err_code=TokenValidatorException.ERR_CODE,
                        ex=position_validation.exception,
                    )
                )
        # Handle the case that the previous_position is flagged.
        previous_position_validation: ValidationResult = ValidationResult.failure(
            CoordValidatorException()
        )
        if token_blueprint.previous_position is not None:
            previous_position_validation = self._position_validator(
                position_candidate=token_blueprint.position
            )
            if previous_position_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenValidatorException.MSG,
                        err_code=TokenValidatorException.ERR_CODE,
                        ex=previous_position_validation.exception,
                    )
                )
        
            
            
        # --- Extract common Token validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        
        # Handle the case that the router did not send a safe Token.
        router_result = self._validation_router.execute(
            id=id,
            team=team,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
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
    