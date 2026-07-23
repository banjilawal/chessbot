# src/builder/model/scalar/builder.py

"""
Module: builder.model.scalar.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import ScalarBlueprint
from builder import ModelBuilder
from err import ScalarBuilderException
from model import Scalar
from result import BuildResult, MethodResultType
from toolkit import ScalarBuilderToolkit
from util import LoggingLevelRouter


class ScalarBuilder(ModelBuilder[Scalar]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Scalar instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[ScalarBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: ScalarBlueprint) -> BuildResult[Scalar]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[ScalarBuilderToolkit] | None = ScalarBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[ScalarBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> ScalarBuilderToolkit:
        return cast(ScalarBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ScalarBlueprint) -> BuildResult[Scalar]:
        """
        Build a safe Scalar.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The ScalarBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Scalar then, send in the success result,
        Args:
            blueprint: ScalarBlueprint
        Returns:
            BuildResult[Scalar]
        Raises:
            ScalarBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuilderException.MSG,
                    err_code=ScalarBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                ScalarBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuilderException.MSG,
                    err_code=ScalarBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Scalar, assembly.payload))