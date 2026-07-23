# src/builder/toggle/vector/builder.py

"""
Module: builder.toggle.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import VectorToggleBlueprint
from builder import ToggleBuilder
from err import VectorToggleBuilderException
from result import BuildResult, MethodResultType
from toggle import VectorToggle
from toolkit import VectorToggleBuilderToolkit
from util import LoggingLevelRouter


class VectorToggleBuilder(ToggleBuilder[VectorToggle]):
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
        builder_toolkit: Optional[VectorToggleBuilderToolkit]

    Provides:
        
        -   _equal_vector_points(point: Point) -> bool
        -  _equal_coord_points(self, point: Point) -> bool
    Super Class:
        ToggleBuilder
    """
    
    def __init__(self, builder_toolkit: Optional[VectorToggleBuilderToolkit] |
                                        None = VectorToggleBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[VectorToggleBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> VectorToggleBuilderToolkit:
        return cast(VectorToggleBuilderToolkit, super().builder_toolkit)
        
    
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
        blueprint_validation = self.builder_toolkit.root_certifier.execute(candidate=blueprint)
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorToggleBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleBuilderException.MSG,
                    err_code=VectorToggleBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(VectorToggleBlueprint, blueprint_validation.payload)
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
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(VectorToggle, assembly.payload))