# src/builder/register/vector/builder.py

"""
Module: builder.register.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import VectorRegisterBlueprint
from builder import RegisterBuilder
from err import VectorRegisterBuilderException
from register import VectorRegister
from result import BuildResult, MethodResultType
from util import LoggingLevelRouter


class VectorRegisterBuilder(RegisterBuilder[VectorRegister]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[VectorRegisterBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: RegisterVectorRegisteBlueprint) -> BuildResult[Register]

     Super Class:
         Builder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[VectorRegisterBuilderToolkit] | 
                           None = VectorRegisterBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[VectorRegisterBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> VectorRegisterBuilderToolkit:
        return cast(VectorRegisterBuilderToolkit, super().builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorRegisterBlueprint) -> BuildResult[VectorRegister]:
        """
        Build a safe VectorRegister.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The bootstrap is not successful.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: VectorRegisterBlueprint
        Returns:
            BuildResult[VectorRegister]
        Raises:
            VectorRegisterBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the bootstrap is not successful.
        blueprint_validation = self.builder_toolkit.bootstrapper.execute(candidate=blueprint)
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorRegisterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuilderException.MSG,
                    err_code=VectorRegisterBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(VectorRegisterBlueprint, blueprint_validation.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorRegisterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuilderException.MSG,
                    err_code=VectorRegisterBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(VectorRegister, assembly.payload))        