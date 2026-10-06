# src/assurance/validator/root/encounter/validator.py

"""
Module: assurance.validator.root.encounter.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    RootValidator, TokenLoader, TokenValidatorToolkit, WalkValidator
)
from domain import (
    Formation, HomeSquare, Team, Token, TokenDeployment,
    TokenPrimeExtract, Walk
)
from err import (
    FormationNullException, RootTokenValidatorException,
    TokenCarrierEmptyException, TokenDeploymentNullException
)
from exchange import TeamValidationRequest, WalkValidationRequest
from transit import RootTokenEnvelope, TeamCarrier, WalkCarrier
from util import IdFactory, LoggingLevelRouter


class RootTokenValidator(RootValidator[Token]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Token super class, then send a RootTokenEnvelope
            for additional processing.

    Attributes:
        loader: TokenLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootTokenEnvelope]

    Super Class:
        RootValidator
    """
    
    def __init__(
            self,
            loader: Optional[TokenLoader] | None = None
    ):
        """
        Args:
            loader: Optional[TokenLoader]
        """
        super().__init__(loader=loader or TokenLoader())
        
    @property
    def loader(self) -> TokenLoader:
        return cast(TokenLoader, super().loader)
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RootTokenEnvelope]:
        """
        Assure a candidate's properties are reference for a Token

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, HomeSquare or Walk are flagged.
            2.  Otherwise, send a TokenProductEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[TokenProductEnvelope]
        Raises:
            RootTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
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
        carrier = prime_extract.carrier
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
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
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- PROCESS_THE_FORMATION_ATTRIBUTE. ---#
        
        # Handle the case that the formation is flagged.
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.formation,
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
        # --- PROCESS_THE_DEPLOYMENT_ATTRIBUTE. ---#
        
        # Handle the case that the deployment is flagged.
        deployment_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.deployment,
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
                item=TeamCarrier(model=blueprint.team),
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
        # --- HOME_SQUARE_DETECTION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.home_square_extractor.execute(
            blueprint=blueprint,
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
        # --- PROCESS_THE_WALK_ATTRIBUTE. ---#
        walk_validation = self.toolkit.wrapper.walk.extract_model(
            request=WalkValidationRequest(
                item=WalkCarrier(model=blueprint.walk),
                id=IdFactory.next_id(class_name="WalkValidationRequest"),
            )
        )
        
        if walk_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RootTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RootTokenValidatorException.MSG,
                    err_code=RootTokenValidatorException.ERR_CODE,
                    ex=walk_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        walk = cast(Walk, walk_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootTokenEnvelope(
            id=id,
            team=team,
            walk=walk,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    