# src/assurance/envelope/producer/rank/producer.py

"""
Module: assurance.envelope.producer.rank.producer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RootEnvelopeProducer, RankValidationLoader, RankLayerToolkit
from domain import Persona, Rank, RankPrimeExtract
from err import (
    PersonaNullException, RankCarrierEmptyException, RankEnvelopeProducerException
)
from transit import RootRankEnvelope
from util import LoggingLevelRouter


class RankEnvelopeProducer(RootEnvelopeProducer[Rank]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs safety checks on Rank super class, then send a 
            RootRankEnvelope for additional processing.

    Attributes:
        loader: RankLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RootRankEnvelope]

    Super Class:
        RootEnvelopeProducer
    """
    
    def __init__(
            self,
            loader: Optional[RankValidationLoader] | None = None
    ):
        """
        Args:
            loader: Optional[RankLoader]
        """
        super().__init__(loader=loader or RankValidationLoader())
    
    @property
    def loader(self) -> RankValidationLoader:
        return cast(RankValidationLoader, super().loader)
    
    @property
    def toolkit(self) -> RankLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RootRankEnvelope]:
        """
        Assure a candidate's properties are reference for a Rank

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Rank, Persona, Deployment, id, or HomeTeam are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a RootRankEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[RootRankEnvelope]
        Raises:
            RootRankEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        loading = self.loader.execute(candidate)
        if loading.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankEnvelopeProducerException.MSG,
                    err_code=RankEnvelopeProducerException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(RankPrimeExtract, loading.payload)
        reference = prime_extract.reference
        blueprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankEnvelopeProducerException.MSG,
                    err_code=RankEnvelopeProducerException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- PROCESS_THE_PERSONA_ATTRIBUTE ---#
        persona_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.persona,
            target_model=Persona,
            null_exception=PersonaNullException(),
        )
        # Handle the case that the deployment is flagged.
        if persona_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankEnvelopeProducerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankEnvelopeProducerException.MSG,
                    err_code=RankEnvelopeProducerException.ERR_CODE,
                    ex=persona_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        persona = cast(Persona, persona_validation.payload)
        
        # --- SEND_THE_WORK_PRODUCT. ---#
        envelope = RootRankEnvelope(
            persona=persona,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(envelope)

    