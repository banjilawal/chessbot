# src/assurance/envelope/producer/token/producer.py

"""
Module: assurance.envelope.producer.token.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RootEnvelopeProducer, TokenLoader, TokenValidatorToolkit
from domain import (
    Footstep, Formation, HomeSquare, Team, Token, TokenDeployment,
    TokenPrimeExtract
)
from err import (
    FormationNullException, TokenCarrierEmptyException,
    TokenDeploymentNullException, TokenEnvelopeProducerException
)
from exchange import FootstepValidationRequest, TeamValidationRequest
from transit import FootstepCarrier, RootTokenEnvelope, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class TokenEnvelopeProducer(RootEnvelopeProducer[Token]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Token super class, then send a 
            RootTokenEnvelope for additional processing.

    Attributes:
        loader: TokenLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootTokenEnvelope]

    Super Class:
        RootEnvelopeProducer
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
                    -   Token, Formation, Deployment, id, or HomeTeam are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a RootTokenEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[RootTokenEnvelope]
        Raises:
            RootTokenEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, loading.payload)
        reference = prime_extract.reference
        blueprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_ID_ATTRIBUTE. ---#
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self.toolkit.nulls.blueprint,
        )
        # Handle the case that any id in the blueprint is flagged.
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- PROCESS_THE_TEAM_ATTRIBUTE. ---#
        team_validation = self.toolkit.wrapper.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=blueprint.team),
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
            )
        )
        # Handle the case that the team is flagged.
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # --- PROCESS_THE_FOOTSTEP_ATTRIBUTE. ---#
        footstep_validation = self.toolkit.wrapper.footstep.extract_model(
            request=FootstepValidationRequest(
                item=FootstepCarrier(model=blueprint.footstep),
                id=IdFactory.next_id(class_name="FootstepValidationRequest"),
            )
        )
        # Handle the case that the footstep is unsafe.
        if footstep_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=footstep_validation.exception,
                )
            )
        # --- PROCESS_THE_DEPLOYMENT_ATTRIBUTE ---#
        deployment_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.deployment,
            target_model=TokenDeployment,
            null_exception=TokenDeploymentNullException(),
        )
        # Handle the case that the deployment is flagged.
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # --- PROCESS_THE_FORMATION_ATTRIBUTE ---#
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        # Handle the case that the deployment is flagged.
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- START_HOME_SQUARE_DETECTION_PROCESS ---#
        home_detection = self.toolkit.home_square_extractor.execute(
            blueprint=blueprint,
        )
        # Handle the case that the home_square gets flagged.
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        footstep = cast(Footstep, footstep_validation.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootTokenEnvelope(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    