# src/fabrication/builder/model/rank/builder.py

"""
Module: fabrication.builder.model.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Bishop, King, Knight, Pawn, Persona, Queen, Rank, RankBlueprint, Rook
from err import RankBuilderException
from exchange import RankBuildRequest
from fabrication import ModelBuilder, RankBuildLoader
from util import LoggingLevelRouter


class RankBuilder(ModelBuilder[Rank]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Rank from a blueprint.

    Attributes:
       loader: RankBuildLoader

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[RankBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[RankBuildLoader]
        """
        super().__init__(loader=loader or RankBuildLoader())
    
    @property
    def loader(self) -> RankBuildLoader:
        return cast(RankBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: RankBuildRequest) -> BuildResult[Rank]:
        """
        Assemble a Rank from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Rank for the success loading.
        Args:
            request: RankBuildRequest
        Returns:
            BuildResult[Rank]
        Raises:
            RankBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuilderException.MSG,
                    err_code=RankBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(RankBlueprint, bootstrap.authorization_applicant)
        persona = blueprint.persona
        
        # --- Send the work product. ---#
        if persona == Persona.BISHOP:
            return BuildResult.success(Bishop())
        if persona == Persona.KING:
            return BuildResult.success(King())
        if persona == Persona.KNIGHT:
            return BuildResult.success(Knight())
        if persona == Persona.PAWN:
            return BuildResult.success(Pawn())
        if persona == Persona.QUEEN:
            return BuildResult.success(Queen())
        return BuildResult.success(Rook())