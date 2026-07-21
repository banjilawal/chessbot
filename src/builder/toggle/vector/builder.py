# src/builder/toggle/vector/builder.py

"""
Module: builder.toggle.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import VectorToggleAssembler
from builder import ToggleBuilder
from result import BuildResult
from err.root import VectorToggleRootCertifier
from toggle import Toggle, VectorToggle
from util import LoggingLevelRouter


class VectorToggleBuilder(ToggleBuilder[Toggle]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Picks toggle a
                -   Coord: Geometric quantity
                -   Vector: Linear Vector
            as an toggle for multiplication, conversion or simple addition.

    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]
        entity: Optional[Coord|Vector]
        is_coord_point: bool
        is_vector_point: bool

    Provides:
        
        -   _equal_vector_points(point: Point) -> bool
        -  _equal_coord_points(self, point: Point) -> bool
    Super Class:
        Toggle
    """
    
    def __init__(
            self,
            assembler: Optional[VectorToggleAssembler] | None = VectorToggleAssembler(),
            bootstrapper: Optional[VectorToggleRootCertifier] | None = VectorToggleRootCertifier(),
    ):
        """
        Args:
            assembler: [VectorToggleAssembler]
            bootstrapper: Optional[VectorToggleRootCertifier]
        """
        super().__init__(bootstrapper=bootstrapper, assembler=assembler)
        
    @property
    def bootstrapper(self) -> VectorToggleRootCertifier:
        return cast(VectorToggleRootCertifier, super().bootstrapper)
    
    @property
    def assembler(self) -> VectorToggleAssembler:
        return cast(VectorToggleAssembler, super().assembler)
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: VectorToggleBlueprint,) -> BuildResult[VectorToggle]:
        """
        Build a safe VectorToggle.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The bootstrap is not successful.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: VectorToggleBlueprint
        Returns:
            BuildResult[VectorToggle]
        Raises:
            VectorToggleBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the bootstrap is not successful.
        bootstrap = self.bootstrapper.execute(candidate=blueprint)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorToggleBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleBuilderException.MSG,
                    err_code=VectorToggleBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=bootstrap.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.assembler.execute(
            blueprint=cast(VectorToggleBlueprint, bootstrap.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorToggleBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleBuilderException.MSG,
                    err_code=VectorToggleBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=self.assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(VectorToggle, assembly.payload))