# src/authorization/adjudicator/chain/priming_validator/adjudicator.py

"""
Module: authorization.adjudicator.chain.priming_validator.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from assurance import PrimingValidator
from authorization import ChainRequest
from err import NullException
from util import LoggingLevelRouter


class ChainAdjudicationBootstrapper:
    """
    Role:
        - Permission Authorization
        -  Checklist Runner
        -  Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a ChainRequest.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Request]

    Super Class:
    """
    _priming_validator: Optional[PrimingValidator]
    _identity_service: Optional[IdentityService]
    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(priming_validator=priming_validator)
    

    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            request_model: Type[ChainRequest],
            request_null_exception: NullException,
            
    ) -> ValidationResult[Request]:
        method = f"{self.__class__.__name__}.execute"
        
        priming = self._priming_validator.execute(
            candidate=candidate,
            target_model=request_model,
            null_exception=request_null_exception,
        )
        if priming.is_failure:
            return ValidationResult.failure(
                exception=VectorNodeSearchRequestException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchRequestException.MSG,
                    err_code=VectorNodeSearchRequestException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        chain_request = cast(ChainRequest, candidate)
        
        id_validation =
        
        chain_validation = self._priming_validator.execute(
            candidate=chain_request,
            target_model=type(chain_adjudicator.chain),
            null_exception=ChainNullException(),
        )
        if chain_validation.is_failure:
            return ValidationResult.failure(
                exception=VectorNodeSearchRequestException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchRequestException.MSG,
                    err_code=VectorNodeSearchRequestException.ERR_CODE,
                    ex=chain_validation.exception,
                )
            )
        return ValidationResult.success(chain_request)
        
        
        