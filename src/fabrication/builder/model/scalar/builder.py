# src/fabrication/builder/model/scalar/builder.py

"""
Module: fabrication.builder.model.scalar.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Scalar, ScalarBlueprint
from err import ScalarBuilderException
from exchange import ScalarBuildRequest
from fabrication import ModelBuilder, ScalarBuildLoader
from util import LoggingLevelRouter


class ScalarBuilder(ModelBuilder[Scalar]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Scalar from a blueprint.

    Attributes:
       loader: ScalarBuildLoader

    Provides:
        -   def execute(blueprint: ScalarBlueprint) -> BuildResult[Scalar]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[ScalarBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[ScalarBuildLoader]
        """
        super().__init__(loader=loader or ScalarBuildLoader())
    
    @property
    def loader(self) -> ScalarBuildLoader:
        return cast(ScalarBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ScalarBuildRequest) -> BuildResult[Scalar]:
        """
        Assemble a Scalar from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Scalar for the success loading.
        Args:
            request: ScalarBuildRequest
        Returns:
            BuildResult[Scalar]
        Raises:
            ScalarBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuilderException.MSG,
                    err_code=ScalarBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(ScalarBlueprint, bootstrap.authorization_applicant)
        
        # --- Send the work product. ---#
        product = Scalar(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)