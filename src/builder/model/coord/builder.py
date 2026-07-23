# src/builder/model/coord/builder.py

"""
Module: builder.model.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import CoordBlueprint
from builder import ModelBuilder
from err import CoordBuilderException
from model import Coord
from result import BuildResult, MethodResultType
from toolkit import CoordBuilderToolkit
from util import LoggingLevelRouter


class CoordBuilder(ModelBuilder[Coord]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Coord instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[CoordBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: CoordBlueprint) -> BuildResult[Coord]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[CoordBuilderToolkit] | None = CoordBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[CoordBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> CoordBuilderToolkit:
        return cast(CoordBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: CoordBlueprint) -> BuildResult[Coord]:
        """
        Build a safe Coord.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The CoordBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Coord then, send in the success result,
        Args:
            blueprint: CoordBlueprint
        Returns:
            BuildResult[Coord]
        Raises:
            CoordBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuilderException.MSG,
                    err_code=CoordBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                CoordBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                CoordBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuilderException.MSG,
                    err_code=CoordBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Coord, assembly.payload))