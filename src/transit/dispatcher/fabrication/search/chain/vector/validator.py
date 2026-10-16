# src/transit/dispatcher/fabrication/search/chain/vector/validator.py

"""
Module: transit.dispatcher.fabrication.search.chain.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from assurance import ChainContextValidator, VectorNodeContextValidator
from domain import VectorNodeContext
from err import VectorNodeContextValidatorException

from util import LoggingLevelRouter


class VectorNodeContextValidator(
    ChainContextValidator[VectorNodeContext]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorNodeContext instance is safe before use.

    Attributes:
        validator: VectorNodeContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[VectorNodeContext]

    Super Class:
        ContextValidator
    """
    
    def __init__(self, validator: VectorNodeContextValidator):
        """
        Args:
            validator: VectorNodeContextChecker
        """
        super().__init__(validator=validator)
    
    
    @property
    def validator(self) -> VectorNodeContextValidator:
        return cast(VectorNodeContextValidator, super().validator)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[VectorNodeContext]:
        """
        Certify a candidate is a VectorNodeContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if validator
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[VectorNodeContext]
        Raises:
            VectorNodeContextValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that validator flags the candidate.
        build = self.validator.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorNodeContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeContextValidatorException.MSG,
                    err_code=VectorNodeContextValidatorException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(VectorNodeContext, build.payload)
        return BuildResult.success(context)

        
    
