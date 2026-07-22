# src/builder/register/vector/builder.py

"""
Module: builder.register.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import VectorRegisterBlueprint
from builder import RegisterBuilder
from register import VectorRegister
from result import BuildResult, MethodResultType
from root import VectorRegisterRootCertifier
from util import LoggingLevelRouter


class VectorRegisterBuilder(RegisterBuilder[VectorRegister]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            assembler: Optional[VectorRegisterAssembler]
            bootstrapper: Optional[VectorRegisterRootCertifier]

    Provides:
        -   def execute(self, blueprint: RegisterVectorRegisteBlueprint) -> BuildResult[Register]

     Super Class:
         Builder
     """
    
    def __init__(
            self,
            assembler: Optional[VectorRegisterAssembler] | None = VectorRegisterAssembler(),
            bootstrapper: Optional[VectorRegisterRootCertifier] | None = VectorRegisterRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorRegisterAssembler],
            bootstrapper: Optional[VectorRegisterRootCertifier]
        """
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
    
    @property
    def bootstrapper(self) -> VectorRegisterRootCertifier:
        return cast(VectorRegisterRootCertifier, super().bootstrapper)
    
    @property
    def assembler(self) -> VectorRegisterAssembler:
        return cast(VectorRegisterAssembler, super().assembler)
    

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
        bootstrap = self._bootstrapper.execute(candidate=blueprint)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorRegisterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuilderException.MSG,
                    err_code=VectorRegisterBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=bootstrap.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self._assembler.execute(
            blueprint=cast(VectorRegisterBlueprint, bootstrap.payload)
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