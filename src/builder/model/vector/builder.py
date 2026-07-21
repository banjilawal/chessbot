# src/builder/model/vector/builder.py

"""
Module: builder.model.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from assembler import VectorAssembler
from blueprint import VectorBlueprint
from builder import ModelBuilder
from err import VectorBuilderException
from model import Vector
from result import BuildResult, MethodResultType
from err.root import VectorRootCertifier
from util import LoggingLevelRouter


class VectorBuilder(ModelBuilder[Vector]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
        
   Responsibilities:
        1.  Ensure a new Vector instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(self, blueprint: VectorBlueprint) -> BuildResult[Vector]
    
     Super Class:
         Builder
     """
    
    def __init__(
            self,
            bootstrapper: VectorRootCertifier | None = VectorRootCertifier(),
            assembler: VectorAssembler | None = VectorAssembler(),
    ):
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
    
    @property
    def bootstrapper(self) -> VectorRootCertifier:
        return cast(VectorRootCertifier, super().bootstrapper)
    
    @property
    def assembler(self) -> VectorAssembler:
        return cast(VectorAssembler, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorBlueprint) -> BuildResult[Vector]:
        """
        Build a safe Vector.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The bootstrap is not successful.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: VectorBlueprint
        Returns:
            BuildResult[Vector]
        Raises:
            VectorBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the bootstrap is not successful.
        bootstrap = self._bootstrapper.execute(candidate=blueprint)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuilderException.MSG,
                    err_code=VectorBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=bootstrap.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self._assembler.execute(
            blueprint=cast(VectorBlueprint, bootstrap.payload)
        )
        if bootstrap.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                VectorBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuilderException.MSG,
                    err_code=VectorBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=bootstrap.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Vector, assembly.payload))