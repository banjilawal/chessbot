# src/transit/route/fabrication/model/square/router.py

"""
Module: transit.route.fabrication.model.square.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import HomeSquareBlueprint, Square, SquareBlueprint
from err import (
    SquareBlueprintNullException, MissingSquareBuildRouteException,
    SquareBuildRouterException
)
from fabrication import (
    HomeSquareSubcontractor,
    BuildRouter, PlainSquareSubcontractor
)
from util import LoggingLevelRouter


class SquareBuildRouter(ModelBuildRouter[Square]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes SquareBlueprint subclasses to the appropriate assembler.

    Attributes:
        home_subcontractor: HomeSquareSubcontractor
        plain_subcontractor: PlainSquareSubcontractor
        
    Provides:
            -   def execute(blueprint: SquareBlueprint) -> BuildResult[Square]

    Super Class:
        BuildRouter
    """
    
    _home_subcontractor: HomeSquareSubcontractor
    _plain_subcontractor: PlainSquareSubcontractor

    
    def __init__(
            self,
            home_subcontractor: Optional[HomeSquareSubcontractor] | None = None,
            plain_subcontractor: Optional[PlainSquareSubcontractor] | None = None,
    ):
        """
        Args:
            home_subcontractor: Optional[HomeSquareSubcontractor]
            plain_subcontractor: Optional[PlainSquareSubcontractor]
        """
        super().__init__()
        self._home_subcontractor = home_subcontractor or HomeSquareSubcontractor()
        self._plain_subcontractor = plain_subcontractor or PlainSquareSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SquareBlueprint) -> BuildResult[Square]:
        """
        Routes a SquareBlueprint to a Subcontractor for construction.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                -   The blueprint is null or the wrong type.
                -   No subcontractor exists for the blueprint.
                -   The subcontractor fails.
            2.  Otherwise, cast the subcontract's product to an Square then send in the
                success result.
        Args:
             blueprint: Blueprint[Square]
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuildRouterException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the case that the router cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=SquareBlueprint,
            null_exception=SquareBlueprintNullException(),
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildRouterException.MSG,
                    err_code=SquareBuildRouterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Otherwise cast the payload for additional prcoessing.
        fingerprint = cast(SquareBlueprint, validation.payload)
        
        # Initialize the default failure result
        result = BuildResult.failure(
            MissingSquareBuildRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=MissingSquareBuildRouteException.MSG,
                err_code=MissingSquareBuildRouteException.ERR_CODE,
            )
        )
        # --- Route to the appropriate square_build subcontractor. ---#
        if isinstance(fingerprint, SquareBlueprint):
            result = self._plain_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, HomeSquareBlueprint):
            result = self._home_subcontractor.execute( fingerprint)
        
        # Handle the case that the subcontractor does make a product.
        if result.is_failure:
            # Handle the case that no route exists for the fingerprint.
            return BuildResult.failure(
                SquareBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildRouterException.MSG,
                    err_code=SquareBuildRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        model = cast(Square, result.payload)
        return BuildResult.success(model)
        
        
        
        