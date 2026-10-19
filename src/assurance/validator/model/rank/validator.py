# src/assurance/validator/model/rank/validator.py

"""
Module: assurance.validator.model.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import RankEnvelopeProducer, ValidationFactory
from domain import Rank
from err import RankValidatorException
from transit import RankCarrier, RankValidationRouter, RootRankEnvelope
from util import LoggingLevelRouter


class RankValidator(ValidationFactory[Rank]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an RankCarrier is safe to use.

    Attributes:
        router: Optional[RankValidationRouter]
        producer: Optional[RankEnvelopeProducer]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[RankCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            router: Optional[RankValidationRouter] | None = None,
            producer: Optional[RankEnvelopeProducer] | None = None,
    ):
        """
        Args:
            router: Optional[RankValidationRouter]
            producer: Optional[RankEnvelopeProducer]
        """
        super().__init__(
            router=router or RankValidationRouter(),
            producer=producer or RankEnvelopeProducer(),
        )
    
    @property
    def router(self) -> RankValidationRouter:
        return cast(RankValidationRouter, super().router)
    
    @property
    def producer(self) -> RankEnvelopeProducer:
        return cast(RankEnvelopeProducer, super().producer)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[RankCarrier]:
        """
        Assure a candidate is a safe RankCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Router fails.
                    -   Team, Formation, Deployment, id, or HomeRank are flagged.
                    -   The producer does not return a product
            2.  Otherwise, send a RankCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RankCarrier]
        Raises:
            RankValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        product = self.producer.execute(candidate=candidate)
        if product.is_failure:
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=product.exception,
                )
            )
        envelope = cast(RootRankEnvelope, product.payload)
        
        validation = self.router.execute(envelope=envelope)
        if validation.is_failure:
            return ValidationResult.failure(
                RankValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorException.MSG,
                    err_code=RankValidatorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        carrier = cast(RankCarrier, validation.payload)
        return ValidationResult.success(carrier)
    