# src/production/resource/producer/model/token/producer.py

"""
Module: production.resource.producer.model.token.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from bootstrap import TokenValidationLoader
from domain import Footstep, Formation, HomeSquare, Team, Token, TokenDeployment, TokenPrimeExtract
from err import (
    FormationNullException, TokenCarrierEmptyException, TokenDeploymentConsistencyException,
    TokenDeploymentNullException,
    TokenEnvelopeProducerException
)
from exchange import FootstepValidationRequest, TeamValidationRequest
from production import EnvelopeProducer
from transit import FootstepCarrier, TokenEnvelope, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class TokenEnvelopeProducer(EnvelopeProducer[Token]):
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
            loader: Optional[TokenValidationLoader] | None = None
    ):
        """
        Args:
            loader: Optional[TokenLoader]
        """
        super().__init__(loader=loader or TokenValidationLoader())
    
    @property
    def loader(self) -> TokenValidationLoader:
        return cast(TokenValidationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[TokenEnvelope]:
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
            item: Any
        Returns:
           ValidationResult[RootTokenEnvelope]
        Raises:
            RootTokenEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(item)
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
        extract = cast(TokenPrimeExtract, loading.payload)
        reference = extract.reference
        fingerprint = reference.extract_blueprint()
        
        # Handle the case that the fingerprint is null
        if fingerprint is None:
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
        id_validation = self.loader.toolkit.blueprint_id_extractor.execute(
            candidate=fingerprint,
            blueprint_owner_name=fingerprint.domain_class_name,
            blueprint_type=self.loader.toolkit.types.blueprint,
            blueprint_null_exception=self.loader.toolkit.nulls.blueprint,
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
        team_validation = self.loader.toolkit.dependency.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=fingerprint.team),
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
        footstep_validation = self.loader.toolkit.dependency.footstep.extract_model(
            request=FootstepValidationRequest(
                item=FootstepCarrier(model=fingerprint.footstep),
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
        deployment_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.deployment,
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
        # Handle the case that there is a deployment inconsistency.
        if fingerprint.has_deployment_inconsistency:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnvelopeProducerException.MSG,
                    err_code=TokenEnvelopeProducerException.ERR_CODE,
                    ex=TokenDeploymentConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenDeploymentConsistencyException.MSG,
                        err_code=TokenDeploymentConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_FORMATION_ATTRIBUTE ---#
        formation_validation = self.loader.toolkit.priming_validator.execute(
            candidate=fingerprint.formation,
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
        home_detection = self.loader.toolkit.home_square_extractor.execute(
            blueprint=fingerprint,
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
        envelope = TokenEnvelope(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            prime_extract=extract,
        )
        return ValidationResult.success(envelope)

    