# src/assurance/validator/validator/roottoken/generator.py

"""
Module: assurance.validator.root.token.generator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    Walk, SafeRootTokenProperties, WalkValidator, TokenProductEnvelope,
    TokenValidatorToolkit, RootValidator
)
from domain import (
    Formation, HomeSquare, Team, Token, TokenBlueprint, TokenDeployment,
    TokenPrimeExtract
)
from err import (
    RootTokenValidatorException, FormationNullException, TokenDeploymentNullException
)
from exchange import TeamValidationRequest
from transit import TeamCarrier
from util import IdFactory, LoggingLevelRouter


class RootTokenValidator(RootValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Token superclass.

    Attributes:
        loader: TokenValidatorToolkit
        position_validator: TokenPositionValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TokenProductEnvelope]:

    Super Class:
        ProductEnvelopeGenerator
    """
    _position_validator: WalkValidator
    
    def __init__(
            self,
            loader: Optional[TokenValidatorToolkit] | None = None,
            position_validator: Optional[ WalkValidator] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenValidatorToolkit]
            position_validator: Optional[TokenPositionValidator]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._position_validator = position_validator or WalkValidator()
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[TokenProductEnvelope]:
        """
        Assure a candidate's properties are reference for a Token

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a TokenProductEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[TokenProductEnvelope]
        Raises:
            TokenProductEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.toolkit.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, loading.payload)
        token_blueprint = cast(TokenBlueprint, prime_extract.blueprint)
        # --- START_ID_VALIDATION_PROCESS ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=token_blueprint,
            blueprint_owner_name=token_blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self.toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- START_FORMATION_VALIDATION_PROCESS ---#
        
        # Handle the case that the formation is flagged.
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- START_DEPLOYEMENT_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the deployment is flagged.
        deployment_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.deployment,
            target_model=TokenDeployment,
            null_exception=TokenDeploymentNullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # --- START_TEAM_VALIDATION_PROCESS ---#
        
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
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # --- START_HOME_SQUARE_DETECTION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.home_square_extractor.execute(
            blueprint=token_blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- START_POSITIONS_VALIDATION_PROCESS ---#
        
        # Handle the case that the current_position is flagged.
        production_result = self._position_validator.execute(
            blueprint=token_blueprint
        )
        if production_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=production_result.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        position_table = cast(Walk, production_result.payload)
        
        safe_properties = SafeRootTokenProperties(
            id=id,
            team=team,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            position_chart=position_table,
        )
        
        # --- Send the work product. ---#
        validation_reference = TokenProductEnvelope(
            safe_properties=safe_properties,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(validation_reference)

    