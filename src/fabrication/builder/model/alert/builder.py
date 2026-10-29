# src/fabrication/builder/model/alert/builder.py

"""
Module: fabrication.builder.model.alert.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Alert, AlertBlueprint
from err import AlertBuilderException
from exchange import AlertBuildRequest
from fabrication import ModelBuilder, AlertBuildLoader
from util import LoggingLevelRouter


class AlertBuilder(ModelBuilder[Alert]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Alert from a blueprint.

    Attributes:
       loader: AlertBuildLoader

    Provides:
        -   def execute(blueprint: AlertBlueprint) -> BuildResult[Alert]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[AlertBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[AlertBuildLoader]
        """
        super().__init__(loader=loader or AlertBuildLoader())
    
    @property
    def loader(self) -> AlertBuildLoader:
        return cast(AlertBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AlertBuildRequest) -> BuildResult[Alert]:
        """
        Assemble a Alert from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Alert for the success loading.
        Args:
            request: AlertBuildRequest
        Returns:
            BuildResult[Alert]
        Raises:
            AlertBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AlertBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertBuilderException.MSG,
                    err_code=AlertBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(AlertBlueprint, bootstrap.payload)
        
        # --- Send the work product. ---#
        product = Alert(
            threat=blueprint.threat,
            checkmate=blueprint.checkmate,
        )
        return BuildResult.success(product)