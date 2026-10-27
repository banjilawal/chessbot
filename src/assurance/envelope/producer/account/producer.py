# src/assurance/envelope/producer/account/producer.py

"""
Module: assurance.envelope.producer.account.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RootEnvelopeProducer, AccountValidationLoader, AccountValidatorToolkit
from domain import Account, AccountPrimeExtract
from err import AccountCarrierEmptyException, AccountEnvelopeProducerException


from transit import RootAccountEnvelope
from util import LoggingLevelRouter


class AccountEnvelopeProducer(RootEnvelopeProducer[Account]):
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
        RootEnvelopeProducer
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
    def toolkit(self) -> AccountValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RootAccountEnvelope]:
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
            candidate: Any
        Returns:
           ValidationResult[RootAccountEnvelope]
        Raises:
            RootAccountEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountEnvelopeProducerException.MSG,
                    err_code=AccountEnvelopeProducerException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(AccountPrimeExtract, loading.payload)
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
            item=blueprint,
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
        id = cast(int, id_validation.payload)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootAccountEnvelope(
            id=id,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    