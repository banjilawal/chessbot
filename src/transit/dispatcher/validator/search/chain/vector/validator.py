# src/transit/dispatcher/validator/search/chain/vector/validator.py

"""
Module: transit.dispatcher.validator.search.chain.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import ChainSearchContextValidator, VectorNodeContextChecker
from domain import VectorNodeContext
from err import VectorNodeContextValidatorException

from util import LoggingLevelRouter


class VectorNodeContextValidator(
    ChainSearchContextValidator[VectorNodeContext]
):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorNodeContext instance is safe before use.

    Attributes:
        integrity_checker: VectorNodeContextChecker

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[VectorNodeContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, integrity_checker: VectorNodeContextChecker):
        """
        Args:
            integrity_checker: VectorNodeContextChecker
        """
        super().__init__(integrity_checker=integrity_checker)
    
    
    @property
    def integrity_checker(self) -> VectorNodeContextChecker:
        return cast(VectorNodeContextChecker, super().integrity_checker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorNodeContext]:
        """
        Certify a candidate is a VectorNodeContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if integrity_checker
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorNodeContext]
        Raises:
            VectorNodeContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that integrity_checker flags the candidate.
        validation = self.integrity_checker.execute(candidate=candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorNodeContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeContextValidatorException.MSG,
                    err_code=VectorNodeContextValidatorException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(VectorNodeContext, validation.payload)
        return ValidationResult.success(context)

        
    
