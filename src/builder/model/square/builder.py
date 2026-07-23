# src/builder/model/square/builder.py

"""
Module: builder.model.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import SquareBlueprint
from builder import ModelBuilder
from err import SquareBuilderException
from model import Square
from result import BuildResult, MethodResultType
from toolkit import SquareBuilderToolkit
from util import LoggingLevelRouter


class SquareBuilder(ModelBuilder[Square]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Square instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[SquareBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: SquareBlueprint) -> BuildResult[Square]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[SquareBuilderToolkit] | None = SquareBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[SquareBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> SquareBuilderToolkit:
        return cast(SquareBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SquareBlueprint) -> BuildResult[Square]:
        """
        Build a safe Square.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The SquareBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Square then, send in the success result,
        Args:
            blueprint: SquareBlueprint
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuilderException.MSG,
                    err_code=SquareBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                SquareBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuilderException.MSG,
                    err_code=SquareBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Square, assembly.payload))