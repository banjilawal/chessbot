# src/transit/dispatcher/builder/toggle/vector/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.toggle.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import CartesianToggleBlueprint
from transit.dispatcher.builder import ToggleBuildDispatcher
from err import CartesianToggleBuilderException
from artifcat import BuildResult, MethodResultType
from domain.structure.toggle import CartesianToggle
from operation.toolkit import CartesianToggleBuilderToolkit
from util import LoggingLevelRouter


class CartesianToggleBuilder(ToggleBuildDispatcher[CartesianToggle]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Picks toggle a
                -  Coord: Geometric quantity
                -  Vector: Linear Vector
            as an toggle for multiplication, conversion or simple addition.

    Attributes:
        builder_toolkit: Optional[CartesianToggleBuilderToolkit]

    Provides:
        
        -  _equal_vector_points(point: Point) -> bool
        -  _equal_coord_points(self, point: Point) -> bool
    Super Class:
        ToggleBuilder
    """
    
    def __init__(self, builder_toolkit: Optional[CartesianToggleBuilderToolkit] |
                                        None = CartesianToggleBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[CartesianToggleBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> CartesianToggleBuilderToolkit:
        return cast(CartesianToggleBuilderToolkit, super().assembler)
        
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CartesianToggleBlueprint,) -> BuildResult[CartesianToggle]:
        """
        Build a safe CartesianToggle.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -  The bootstrap is not successful.
                    -  The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: CartesianToggleBlueprint
        Returns:
            BuildResult[CartesianToggle]
        Raises:
            CartesianToggleBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the bootstrap is not successful.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(candidate=blueprint)
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CartesianToggleBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleBuilderException.MSG,
                    err_code=CartesianToggleBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(CartesianToggleBlueprint, blueprint_validation.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CartesianToggleBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleBuilderException.MSG,
                    err_code=CartesianToggleBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(CartesianToggle, assembly.payload))