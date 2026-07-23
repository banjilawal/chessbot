# src/builder/model/snapshot/builder.py

"""
Module: builder.model.snapshot.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import SnapshotBlueprint
from builder import ModelBuilder
from err import SnapshotBuilderException
from model import Snapshot
from result import BuildResult, MethodResultType
from toolkit import SnapshotBuilderToolkit
from util import LoggingLevelRouter


class SnapshotBuilder(ModelBuilder[Snapshot]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Snapshot instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[SnapshotBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: SnapshotBlueprint) -> BuildResult[Snapshot]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[SnapshotBuilderToolkit] | None = SnapshotBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[SnapshotBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> SnapshotBuilderToolkit:
        return cast(SnapshotBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SnapshotBlueprint) -> BuildResult[Snapshot]:
        """
        Build a safe Snapshot.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The SnapshotBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Snapshot then, send in the success result,
        Args:
            blueprint: SnapshotBlueprint
        Returns:
            BuildResult[Snapshot]
        Raises:
            SnapshotBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SnapshotBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SnapshotBuilderException.MSG,
                    err_code=SnapshotBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                SnapshotBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                SnapshotBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SnapshotBuilderException.MSG,
                    err_code=SnapshotBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Snapshot, assembly.payload))