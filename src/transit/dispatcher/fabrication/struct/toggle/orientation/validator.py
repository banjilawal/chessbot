# src/transit/dispatcher/fabrication/model/struct/register/operand/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.register.operand.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from selector import OrientationToggle
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import ModelBuildDispatcher


class OrientationSelectorBuildDispatcher(ModelBuildDispatcher[OrientationToggle]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Build Process Owner

    Responsibilities:
        1.  Ensure a OrientationOperand instance is certified safe, reliable, and consistent
            before use.

    Attributes:
        carrier_builder: CartesianToggleRegisterBuilder

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : OrientationOperandToolkit,
            ) -> BuildResult[OrientationOperand]:

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            builder: CartesianToggleRegisterBuilder | None = CartesianToggleRegisterBuilder(),
    ):
        super().__init__(builder=builder)
        
    @property
    def builder(self) -> CartesianToggleRegisterBuilder:
        return cast(CartesianToggleRegisterBuilder, super().builder)
    
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult:
        """
        Verify the candidate is a safe OrientationOperand.
        
        Action:
            1.  Send an exception in the BuildResult any of these
                conditions occur.
                    - candidate is null.
                    - It's not a OrientationOperand.
                    - The orientationOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            job: Any
        Returns:
            BuildResult
        Raises:
            OrientationOperandBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that the builder is not primed.
        builder_priming_result = self.builder.bundle.priming_builder.execute(
            job=job,
            target_model=self.builder.bundle.model,
            context_null_exception=self.builder.bundle.request_null_exception,
        )
        if builder_priming_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                OrientationOperandBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=OrientationOperandBuilderException.MSG,
                    err_code=OrientationOperandBuilderException.ERR_CODE,
                    ex=builder_priming_result.exception
                )
            )
        # --- Cast candidate to a OrientationOperand for additional tests. ---#
        register = cast(OrientationOperandEntityRegister, job)
        
        root_build = self.builder.execute(register)
        if root_build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                OrientationOperandBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=OrientationOperandBuilderException.MSG,
                    err_code=OrientationOperandBuilderException.ERR_CODE,
                    ex=root_build.exception
                )
            )
        
        return root_build

            