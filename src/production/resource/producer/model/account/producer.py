# src/production/resource/producer/model/account/producer.py

"""
Module: production.resource.producer.model.account.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from domain import Account, AccountPrimeExtract
from err import AccountCarrierEmptyException, AccountEnvelopeProducerException
from production import ModelEnvelopeProducer

from transit import AccountEnvelope
from util import LoggingLevelRouter


class AccountEnvelopeProducer(ModelEnvelopeProducer[Account]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Account super class, then send a 
            RootAccountEnvelope for additional processing.

    Attributes:
        loader: AccountLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootAccountEnvelope]

    Super Class:
        EnvelopeProducer
    """
    
    def __init__(
            self,
            loader: Optional[AccountValidationLoader] | None = None
    ):
        """
        Args:
            loader: Optional[AccountLoader]
        """
        super().__init__(loader=loader or AccountValidationLoader())
    
    @property
    def loader(self) -> AccountValidationLoader:
        return cast(AccountValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[AccountEnvelope]:
        """
        Assure a candidate's properties are reference for a Account

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Account, Formation, Deployment, id, or HomeTeam are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a RootAccountEnvelope in the success result.
        Args:
            item: Any
        Returns:
           ValidationResult[RootAccountEnvelope]
        Raises:
            RootAccountEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(item)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEnvelopeProducerException.MSG,
                    err_code=AccountEnvelopeProducerException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(AccountPrimeExtract, bootstrap.authorization_applicant)
        reference = prime_extract.reference
        blueprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEnvelopeProducerException.MSG,
                    err_code=AccountEnvelopeProducerException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
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
                AccountEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEnvelopeProducerException.MSG,
                    err_code=AccountEnvelopeProducerException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = cast(int, id_validation.authorization_applicant)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = AccountEnvelope(
            id=id,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    